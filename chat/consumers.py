from channels.generic.websocket import JsonWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Chat
from .serializers import ChatSerializer



class ChatConsumer(JsonWebsocketConsumer):

    def has_access_permission(self):
        try:
            if str(self.scope["user"].id) not in self.room_name.split("_"):
                return False
            else:
                self.scope["room_name"] = self.room_name
                return True
        except Exception as e:
            return False
    
    def new_message(self, content):
        return_data = {}
        return_data["type"]="message"
        create_message = Chat.objects.create(
            sender_id=content["sender"],
            receiver_id=content["receiver"],
            message = content["message"]
        )
        return_data["data"] = ChatSerializer(Chat.objects.filter(sender__id=content["sender"],
            receiver__id=content["receiver"]).all().order_by("date_created"), many=True).data
        self.chat_message(return_data)


    def next_event(self, content):
        return_data = {
            "type":"next",
            "data":{}
        }
        self.chat_message(return_data)

    commands = {
        "message": new_message,
        "next": next_event,
    }

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)

        print("user_has_access_permission:-", self.has_access_permission())
        if self.has_access_permission():
            self.accept()
        else:
            self.close()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name, self.channel_name
        )
    
    def receive_json(self, content, **kwargs):
        self.commands[content["type"]](self, content)
    
    @staticmethod
    def external_group_send(room_name, content):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(room_name), {"type": "chat_message", "content": content}
        )
    
    def group_send(self, content):
        async_to_sync(self.channel_layer.group_send)(
            self.room_name, {"type": "chat_message", "content": content}
        )

    def chat_message(self, event):
        content = event["content"]
        self.send_json(content)
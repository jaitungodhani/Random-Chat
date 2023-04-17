from rest_framework.serializers import ModelSerializer
from account.serializers import UserSerializer
from .models import Chat
from .models import Room

class ChatSerializer(ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    class Meta:
        model = Chat
        fields = "__all__"

class RoomSerialzer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
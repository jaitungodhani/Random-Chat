from rest_framework.serializers import ModelSerializer
from account.serializers import UserSerializer
from .models import Chat

class ChatSerializer(ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    class Meta:
        model = Chat
        fields = "__all__"


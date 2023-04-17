from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data= super().validate(attrs)
        if self.user.is_login == True:
            raise Exception("You are login in some other device first you need to logout!!!")
        self.user.is_login = True
        self.user.is_chatting = False
        self.user.save()
        data["user_data"] = {
            "id": self.user.id,
            "username": self.user.username,
            "is_active" : self.user.is_active,
            "is_chatting" : self.user.is_chatting,
            "profile_picture": self.user.profile_picture.url if self.user.profile_picture else None
        }
        return data
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = [
            "is_chatting",
            "is_superuser",
            "is_active",
            "is_login",
            "is_staff",
            "last_login"
        ]
        extra_kwargs = {
            "password": {'write_only': True}
        }

    def create(self, validated_data):
        self.password = validated_data.pop("password")
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(self.password)
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = [
            "is_chatting",
            "is_superuser",
            "is_active",
            "is_login",
            "is_staff",
            "last_login",
            "email"
        ]
        extra_kwargs = {
            "password": {'write_only': True}
        }
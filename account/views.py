from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializers import (
    LoginSerializer,
    UserSerializer,
    UserUpdateSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView    
from utils.response_handler import ResponseMsg 
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
import random
from chat.models import (
    Chat,
    Room
)
from django.db.models import Q
from chat.serializers import RoomSerialzer


User = get_user_model()

# Create your views here.
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        response_data = super().post(request, *args, **kwargs)
        response = ResponseMsg(
            data=response_data.data,
            error=False,
            message="Login Successfully!!!!"
        )
        return Response(response.response)


class LogoutView(ViewSet):
    def list(self, request):
        request.user.is_login = False
        request.user.is_chatting = False
        request.user.save()
        Room.objects.filter(Q(user_1=request.user) | Q(user_2=request.user)).delete()
        response = ResponseMsg(
            data={},
            error=False,
            message="Logout Successfully!!!!"
        )
        return Response(response.response)


class UserManageView(ViewSet):
    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
        return super(UserManageView, self).get_permissions()

    @swagger_auto_schema(
            request_body=UserSerializer
    )
    def create(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseMsg(
            data=serializer.data,
            error=False,
            message="Create User Successfully!!!!"
        )
        return Response(response.response)
    
    @swagger_auto_schema(
            request_body=UserUpdateSerializer
    )
    def update(self, request, pk=None):
        if int(pk) != request.user.id:
            raise PermissionError("You do not have permission to perform this action")
        try:
            user_obj = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Exception("User Not Found For particular Id!!!")
        serializer = UserUpdateSerializer(user_obj, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseMsg(
            data=serializer.data,
            error=False,
            message="Update User Successfully!!!!"
        )
        return Response(response.response)
        

    @action(
        methods=["GET"],
        detail=False
    )
    def random_user_select(self, request):
        room_obj = Room.objects.filter(Q(user_1=request.user) | Q(user_2=request.user)).first()

        if room_obj:
            random_user = User.objects.filter(Q(id = room_obj.user_1.id) | Q(id = room_obj.user_2.id)).exclude(id=request.user.id).first()
    
            room_serializer = RoomSerialzer(
              room_obj
            )
        else:
            all_user = list(User.objects.filter(is_chatting=False, is_login=True).all().exclude(Q(id=request.user.id) | Q(is_superuser=True)))
            random_user = random.choice(all_user)
            request.user.is_chatting = True
            random_user.is_chatting= True
            random_user.save()
            request.user.save()
            room_serializer = RoomSerialzer(
            data={
            "name": f"{request.user.id}_{random_user.id}",
            "user_1":request.user.id,
            "user_2":random_user.id
            }
            )
            room_serializer.is_valid(raise_exception=True)
            room_serializer.save()

        serializer = UserSerializer(random_user)
        
        response = ResponseMsg(
            data={
                "random_user":serializer.data,
                "room_data":room_serializer.data
            },
            error=False,
            message="Random User Get Successfully!!!!"
        )
        return Response(response.response)

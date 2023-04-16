from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .user_manager import CustomUserManager
from random_chat.behaviour import DateMixin

class User(DateMixin, AbstractBaseUser):
    username = models.CharField(
        verbose_name=_("UserName"),
        max_length=200
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True
    )
    is_chatting = models.BooleanField(
        verbose_name=_("Is Chatting"),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=_("Is SuperUser"),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_("Is Active"),
        default=True
    )
    is_login = models.BooleanField(
        verbose_name=_("Is Login"),
        default=False
    )
    profile_picture = models.ImageField(
        verbose_name=_("Profile_Picture"),
        upload_to="profile_picture",
        null=True,
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name=_("Is Staff"),
        default=True
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        ordering = ('id',)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.username + "-----" + str(self.id)
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
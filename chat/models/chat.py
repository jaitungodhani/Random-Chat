from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from random_chat.behaviour import DateMixin

User = get_user_model()

class Chat(DateMixin, models.Model):
    sender = models.ForeignKey(
        User,
        verbose_name=_("Sender"),
        related_name="msg_sender",
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        verbose_name=_("Receiver"),
        related_name="msg_receiver",
        on_delete=models.CASCADE
    )
    message = models.CharField(
        verbose_name=_("message"),
        max_length=200
    )

    def __str__(self) -> str:
        return self.room_name + "--" + str(self.owner.id) + "--" + str(self.message)
    
    class Meta:
        ordering = ('id',)
        verbose_name = "Chat"
        verbose_name_plural = "Chats"
    
    
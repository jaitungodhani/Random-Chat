from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User

class Room(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150,
        unique=True
    )
    user_1 = models.ForeignKey(
        User,
        verbose_name=_("User 1"),
        on_delete=models.CASCADE,
        related_name="User1"
    )
    user_2 = models.ForeignKey(
        User,
        verbose_name=_("User 2"),
        on_delete=models.CASCADE,
        related_name="User2"
    )

    def __str__(self) -> str:
        return self.name
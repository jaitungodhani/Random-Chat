# Generated by Django 4.2 on 2023-04-16 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='room_name',
        ),
        migrations.AddField(
            model_name='chat',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='msg_receiver', to=settings.AUTH_USER_MODEL, verbose_name='Receiver'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='msg_sender', to=settings.AUTH_USER_MODEL, verbose_name='Sender'),
            preserve_default=False,
        ),
    ]

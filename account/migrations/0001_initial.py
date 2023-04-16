# Generated by Django 4.2 on 2023-04-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('username', models.CharField(max_length=200, verbose_name='UserName')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is SuperUser')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_picture', verbose_name='Profile_Picture')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ('id',),
            },
        ),
    ]
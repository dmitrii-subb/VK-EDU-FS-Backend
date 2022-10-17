from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Message(models.Model):
    text = models.TextField(max_length=1024)
    date = models.DateTimeField()
    author = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)


class Chat(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    messages = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL)


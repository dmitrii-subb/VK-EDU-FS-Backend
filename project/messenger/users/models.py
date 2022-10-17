from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL


class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)

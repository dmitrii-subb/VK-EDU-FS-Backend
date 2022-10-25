from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)
    birtday = models.DateField('Дата рождения', null=True, blank=True)
    email = models.EmailField('Email', null=True, blank=True)
    about = models.TextField('О себе', max_length=1024, blank=True)

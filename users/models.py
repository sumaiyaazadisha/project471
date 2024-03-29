from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        app_label = 'users'


class Admin(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)


    def __str__(self):
        return self.username

# Create your models here.

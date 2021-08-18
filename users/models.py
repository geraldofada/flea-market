from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=11)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
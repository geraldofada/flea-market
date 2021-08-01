from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=30, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname

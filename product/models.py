from django.db import models
from category.models import Category
from login.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100)
    image = models.CharField(max_length=150, blank=True)
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ManyToManyField(Category)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Awnser(models.Model):
    text = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
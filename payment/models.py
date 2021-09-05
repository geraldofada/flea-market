import uuid
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from users.models import User
from product.models import Product


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=12, decimal_places=2, default=1)
    product_small_description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.owner.username}_{self.product_name}'

class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=12, decimal_places=2, default=1)
    product_small_description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.owner.username}_{self.product_name}'
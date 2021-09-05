from product.models import Product
import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from users.models import User


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    owner = models.OneToOneField(User, on_delete=CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.owner.username
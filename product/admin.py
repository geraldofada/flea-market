from django.contrib import admin
from product import models
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Answer)
admin.site.register(models.Question)
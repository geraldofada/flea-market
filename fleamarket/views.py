from product.models import Product
from django.shortcuts import render
from category.models import Category
from product.models import Product

def index(request):
    categories = Category.objects.all().order_by('name')
    products = Product.objects.all().filter(quantity__gt=0).order_by('-created_at')
    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'index.html', context)
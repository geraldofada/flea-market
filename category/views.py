from django.shortcuts import render
from product.models import Product
from category.models import Category


def products_by_category(request, slug):
    categories = Category.objects.all()

    category = categories.get(slug=slug)
    products = Product.objects.all().filter(category=category.id)

    context = {
        'categories': categories,
        'products': products,
        'category': category
    }

    return render(request, 'category/products_by_category.html', context)
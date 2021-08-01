from django.shortcuts import render
from category.models import Category

def index(request):
    categories = Category.objects.all().order_by('name')
    context = {
        'categories': categories
    }

    return render(request, 'index.html', context)
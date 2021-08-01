from django.shortcuts import render
from category.models import Category


def login(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'login/login.html', context)

def signup(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'login/signup.html', context)
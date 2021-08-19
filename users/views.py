from django.shortcuts import render

from category.models import Category
from users.forms import UserCreationForm, UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
    else:
        form = UserLoginForm()

    categories = Category.objects.all()

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'users/login.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()

    categories = Category.objects.all()

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'users/signup.html', context)
from django.contrib.messages.api import success
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate

from category.models import Category
from users.forms import UserCreationForm, UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = form.data['username']
        password = form.data['password']

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return redirect('users:login')
    else:
        form = UserLoginForm()

    categories = Category.objects.all()

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'users/login.html', context)

def logout(request):
    auth_logout(request)
    messages.success(request, 'Usuário deslogado.')
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('/')
        else:
            messages.error(request, form.errors)
            
    else:
        form = UserCreationForm()

    categories = Category.objects.all()

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'users/signup.html', context)
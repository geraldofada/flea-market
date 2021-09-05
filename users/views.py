from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.decorators import login_required

from category.models import Category
from users.forms import UserCreationForm, UserLoginForm
from cart.models import Cart

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

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, 'Usuário deslogado.')
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            cart = Cart(owner=user)
            cart.save()
            messages.success(request, 'Usuário criado com sucesso!')
            auth_login(request, user)
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
from django.http.response import JsonResponse
from product.models import Product
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from product.models import Product
from category.models import Category
from cart.models import Cart


@login_required
def show(request):
    categories = Category.objects.all()
    cart = Cart.objects.get(owner=request.user).products.all()

    total = 0
    for prod in cart:
        total += prod.price

    context = {
        'categories': categories,
        'total': total,
        'cart': cart
    }

    return render(request, 'cart/show.html', context)

@login_required
def add(request, id):
    if request.method == 'GET':
        cart = Cart.objects.get(owner=request.user)
        product = Product.objects.get(pk=id)
        cart.products.add(product)
        cart.save()

        return redirect('cart:show')

@login_required
def delete(request):
    if request.method == 'GET':
        id = request.GET.get('prodId')
        product = Product.objects.get(pk=id)
        cart = Cart.objects.get(owner=request.user)
        cart.products.remove(product)
        cart.save()

        new_total = 0
        for prod in cart.products.all():
            new_total += prod.price

        return JsonResponse({
            'removedId': id,
            'newTotal': new_total
        })
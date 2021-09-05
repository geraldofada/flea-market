from cart.models import Cart
from django.core.paginator import Paginator
from django.http.response import JsonResponse
from django.contrib import messages
from product.models import Product
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from product.models import Product
from category.models import Category
from payment.models import Purchase
from django.urls import reverse


@login_required
def purchase_show(request):
    categories = Category.objects.all()
    purchase = Purchase.objects.all().filter(owner=request.user).order_by('-created_at')

    page = request.GET.get('page')
    paginator = Paginator(purchase, 6)
    purchase_obj = paginator.get_page(page)

    context = {
        'categories': categories,
        'purchase': purchase_obj
    }

    return render(request, 'payment/purchase_show.html', context)

@login_required
def sale_show(request):
    categories = Category.objects.all()
    purchase = Purchase.objects.all().filter(owner=request.user).order_by('-created_at')

    page = request.GET.get('page')
    paginator = Paginator(purchase, 6)
    purchase_obj = paginator.get_page(page)

    context = {
        'categories': categories,
        'purchase': purchase_obj
    }

    return render(request, 'payment/purchase_show.html', context)

@login_required
def buy(request, id):
    if request.method == 'GET':
        product = Product.objects.get(pk=id)
        if product.quantity > 0:
            product.quantity -= 1

            purchase = Purchase(
                owner=request.user,
                product=product,
                product_name=product.name,
                product_price=product.price,
                product_small_description=product.small_description
            )

            product.save()
            purchase.save()

            messages.success(request, 'Produto comprado com sucesso!')

            return redirect('payment:purchase_show')

@login_required
def close_cart(request):
    if request.method == 'POST':
        cart = Cart.objects.get(owner=request.user)
        product_ids = request.POST.getlist('productIds[]')
        purchase_ok = False
        for id in product_ids:
            product = Product.objects.get(pk=id)
            if product.quantity > 0:
                purchase_ok = True
                product.quantity -= 1

                purchase = Purchase(
                    owner=request.user,
                    product=product,
                    product_name=product.name,
                    product_price=product.price,
                    product_small_description=product.small_description
                )

                cart.products.remove(product)

                cart.save()
                product.save()
                purchase.save()

        if purchase_ok:
            messages.success(request, 'Compra finalizada com sucesso!')
            res = {
                'url': reverse('payment:purchase_show'),
            }
        else:
            messages.error(request, 'Pedido fora de estoque :(')
            res = {
                'url': reverse('cart:show'),
            }
        return JsonResponse(res)

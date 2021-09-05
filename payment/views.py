from django.core.paginator import Page, Paginator
from django.http.response import JsonResponse
from django.contrib import messages
from product.models import Product
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from product.models import Product
from category.models import Category
from payment.models import Purchase


@login_required
def show(request):
    categories = Category.objects.all()
    purchase = Purchase.objects.all().filter(owner=request.user).order_by('-created_at')

    paginator = Paginator(purchase, 6)
    purchase_obj = paginator.get_page(Page)

    context = {
        'categories': categories,
        'purchase': purchase_obj
    }

    return render(request, 'payment/show.html', context)

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

            return redirect('payment:show')

@login_required
def close_cart(request):
    if request.method == 'POST':
        product_ids = request.POST.get('productIds')
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

                product.save()
                purchase.save()

        if purchase_ok:
            messages.success(request, 'Compra finalizada com sucesso!')
            return redirect('payment:show')
        else:
            messages.error(request, 'Produtos fora de estoque :(')
            return redirect('cart:show')

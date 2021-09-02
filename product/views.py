from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from product.models import Awnser, Product, Question
from product.forms import ProductForm
from category.models import Category


def product_by_id(request, id):
    categories = Category.objects.all()

    product = get_object_or_404(Product, pk=id)

    questions = []
    questionsQuery = Question.objects.filter(product=id)
    if questionsQuery:
        for q in questionsQuery:
            question_awnser = []
            question_awnser.append(q)

            awnser = Awnser.objects.filter(question=q.id)
            if awnser:
                question_awnser.append(awnser[0])

            questions.append(question_awnser)

    context = {
        'categories': categories,
        'product': product,
        'questions': questions,
    }

    return render(request, 'product/product_by_id.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.owner = request.user
            product.save()

            messages.success(request, 'Produto criado com sucesso.')
            return redirect('product:product_by_id', id=product.id)
        else:
            messages.error(request, form.errors)
    else:
        form = ProductForm()

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'form': form
    }

    return render(request, 'product/create.html', context)

@login_required
def edit(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.owner = request.user
            product.save()

            messages.success(request, 'Produto atualizado com sucesso.')
            return redirect('product:product_by_id', id=product.id)
        else:
            messages.error(request, form.errors)
    else:
        form = ProductForm(instance=product)

    categories = Category.objects.all()
    context = {
        'product_id': id,
        'categories': categories,
        'form': form
    }

    return render(request, 'product/edit.html', context)

@login_required
def delete(request):
    if request.method == 'GET':
        id = request.GET.get('prodId')
        product = Product.objects.get(pk=id)
        product.image.delete()
        product.delete()
        return JsonResponse({
            'removedId': id,
        })

@login_required
def list_by_user(request):
    categories = Category.objects.all().order_by('name')

    page = request.GET.get('page')
    products = Product.objects.all()
    products = Product.objects.all().filter(owner_id=request.user.id)
    paginator = Paginator(products, 6)
    prod_obj = paginator.get_page(page)
    context = {
        'categories': categories,
        'products': prod_obj,
    }

    return render(request, 'product/list_by_user.html', context)
from django.http.response import HttpResponseBadRequest, JsonResponse
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

def list_by_name(request):
    categories = Category.objects.all()

    products = []
    if request.method == 'POST':
        name = request.POST.get('name')
        products = Product.objects.all().filter(name__contains=name)

    context = {
        'categories': categories,
        'products': products,
        'name': name
    }

    return render(request, 'product/list_by_name.html', context)

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

    form = ProductForm()

    page = request.GET.get('page')
    products = Product.objects.all().filter(owner_id=request.user.id).order_by('-created_at')
    paginator = Paginator(products, 6)
    prod_obj = paginator.get_page(page)

    total_per_page = 0
    for prod in prod_obj:
        total_per_page += (prod.price * prod.quantity)

    context = {
        'categories': categories,
        'products': prod_obj,
        'form': form,
        'total_per_page': total_per_page
    }

    return render(request, 'product/list_by_user.html', context)

@login_required
def fast_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)
            product.owner = request.user
            product.save()

            res = {
                'id': product.id,
                'price': product.price,
                'quantity': product.quantity,
                'small_description': product.small_description,
                'name': product.name,
            }

            return JsonResponse(res, safe=False)
        else:
            return HttpResponseBadRequest(form.errors.as_json(), content_type="application/json")

@login_required
def update_quantity(request):
    if request.method == 'POST':
        id = request.POST.get('prodId')
        quantity = request.POST.get('quantity')
        # limit = int(request.POST.get('limit'))

        product = Product.objects.get(pk=id)
        product.quantity = quantity
        product.save()

        # total_price = Product.objects.all().filter(owner_id=request.user.id).order_by('-created_at')[:limit].aggregate(sum=Sum(F('price') * F('quantity')))

        return JsonResponse({
            # 'total_price': float(total_price['sum'])
        })

@login_required
def create_question(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        if (request.user == product.owner):
            messages.error(request, 'Não é possível fazer perguntas no próprio anúncio.')
        else:
            question = request.POST.get('question')
            if question == '':
                return redirect('product:product_by_id', id=id)
            
            new_question = Question(text=question, owner=request.user, product=product)
            new_question.save()
            messages.success(request, 'Pergunta criada com sucesso.')
            

    return redirect('product:product_by_id', id=id)
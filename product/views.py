from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib import messages
from product.models import Awnser, Product, Question
from login.models import User
from product.forms import CreateForm
from category.models import Category


def product_by_id(request, id):
    categories = Category.objects.all()

    product = Product.objects.get(id=id)

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

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.slug = slugify(product.name)

            #TODO(Geraldo): quando concluir o modelo de usuário, mudar aqui
            user = User.objects.get(pk=1)
            product.owner = user
            product.save()

            messages.success(request, 'Product created with success.')
            return redirect('product:product_by_id', id=product.id)
    else:
        form = CreateForm()

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'form': form
    }

    return render(request, 'product/create.html', context)

def list_by_user(request):
    categories = Category.objects.all().order_by('name')

    #TODO(Geraldo): essa parte vai precisar de permissões do usuário logado
    page = request.GET.get('page')
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    prod_obj = paginator.get_page(page)
    context = {
        'categories': categories,
        'products': prod_obj,
    }

    return render(request, 'product/list_by_user.html', context)
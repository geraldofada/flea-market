from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from product.models import Awnser, Product, Question
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
            return HttpResponseRedirect('/')
    else:
        form = CreateForm()

    categories = Category.objects.all()
    context = {
        'categories': categories,
        'form': form
    }

    return render(request, 'product/create.html', context)
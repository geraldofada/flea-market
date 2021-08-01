from django.shortcuts import render
from product.models import Awnser, Product, Question
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
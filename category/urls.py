from django.urls import path
from category import views


app_name = 'category'

urlpatterns = [
    path('<slug:slug>/', views.products_by_category, name='products_by_category'),
]
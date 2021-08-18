from django.urls import path
from product import views


app_name = 'product'

urlpatterns = [
    path('<int:id>/', views.product_by_id, name='product_by_id'),
    path('create/', views.create, name='create'),
    path('list/', views.list_by_user, name='list_by_user'),
]

from django.urls import path
from product import views


app_name = 'product'

urlpatterns = [
    path('<int:id>/', views.product_by_id, name='product_by_id'),
    path('create/', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('list/', views.list_by_user, name='list_by_user'),
    path('list_by_name/', views.list_by_name, name='list_by_name'),
    path('delete/', views.delete, name='delete'),
    path('fast_create/', views.fast_create, name='fast_create'),
    path('update_quantity/', views.update_quantity, name='update_quantity'),
    path('create_question/<int:id>', views.create_question, name='create_question'),
]

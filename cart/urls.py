from django.urls import path
from cart import views


app_name = 'cart'

urlpatterns = [
    path('', views.show, name='show'),
    path('add/<uuid:id>', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
]
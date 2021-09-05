from django.urls import path
from payment import views


app_name = 'payment'

urlpatterns = [
    path('purchase/', views.purchase_show, name='purchase_show'),
    path('sale/', views.sale_show, name='sale_show'),
    path('buy/<uuid:id>', views.buy, name='buy'),
    path('close_cart/', views.close_cart, name='close_cart'),
]
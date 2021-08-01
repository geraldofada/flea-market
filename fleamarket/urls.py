from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from fleamarket import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('login.urls')),
    path('product/', include('product.urls')),
    path('category/', include('category.urls')),
    path('admin/', admin.site.urls),
]

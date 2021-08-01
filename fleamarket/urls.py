from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from fleamarket import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', include('category.urls')),
    path('admin/', admin.site.urls),
]

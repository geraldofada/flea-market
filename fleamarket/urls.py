from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from fleamarket import views, settings

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('login.urls')),
    path('product/', include('product.urls')),
    path('category/', include('category.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
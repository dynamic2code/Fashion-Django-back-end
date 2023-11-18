from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import category_list, product_list, product_image_list

urlpatterns = [
    path('api/categories/', category_list, name='category-list'),
    path('api/products/', product_list, name='product-list'),
    path('api/product-images/', product_image_list, name='product-image-list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('', views.tryf, name='index'),
    path('see/',views.product_list, name= 'product'),
    path('shop/',views.product_list_shop, name= 'shop_product'),
    path('success/', views.addProduct, name= 'addP'),
    path('alter/<int:product_id>/', views.edit, name='edit'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update-product/<int:product_id>/', views.update_product, name='update_product'),
    path('product/<int:product_id>/', views.show_product, name='show_product'),
    path('combo/',views.p, name= 'combo_add'),
    path('add_combo/', views.add_combo, name='add_combo'),
    path('combov/', views.see_combo),
    path('combosee/', views.combo_detail, name='combo_detail'),
    path('index/',views.blog_detail),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
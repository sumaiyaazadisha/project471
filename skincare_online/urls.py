
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testing.urls')),
    path('', include('users.urls')),
    path('video/', include('video.urls')),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),
    path('skin_product/', include('testing.urls')),
    path('hair_product/', include('testing.urls')),
    path('makeup_product/', include('testing.urls')),
    path('others_product/', include('testing.urls')),


]


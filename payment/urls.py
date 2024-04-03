from django.urls import path
from payment.views import checkout,apply_coupon

urlpatterns = [
    path('checkout',checkout,name="checkout"),
    path('apply-coupon',apply_coupon,name="apply_coupon"),
]
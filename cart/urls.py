
from django.urls import path
from cart.views import add_to_cart,cart_view,increment_quantity,decrement_quantity,remove_quantity

urlpatterns = [
    path("add-to-cart/<int:id>/",add_to_cart,name="add_to_cart"),
    path("cart-view",cart_view,name="my_cart"),
    path("increment-quantity/<int:id>/",increment_quantity,name="increment_quantity"),
    path("decrement-quantity/<int:id>/",decrement_quantity,name="decrement_quantity"),
    path("remove-quantity/<int:id>/",remove_quantity,name="remove_quantity"),
]
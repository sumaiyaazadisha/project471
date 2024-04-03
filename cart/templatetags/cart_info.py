from django import template
register = template.Library()
from cart.models import Cart,Order

@register.filter
def cart_count(request):
    num_cart = Cart.objects.filter(user=request.user,purchased=False)
    return num_cart.count()

@register.filter
def cart_itemlist(request):
    num_cart = Cart.objects.filter(user=request.user,purchased=False)
    return num_cart
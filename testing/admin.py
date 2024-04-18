from django.contrib import admin

# Register your models here.
from testing.models import Product, ProductRating,combo

# Register your models here.

admin.site.register(Product)
admin.site.register(combo)
admin.site.register(ProductRating)

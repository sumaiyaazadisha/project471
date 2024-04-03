from django.db import models
from django.contrib.auth.models import User
from testing.models import Product
from django.utils import timezone
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_cart")
    cart_product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="user_product")
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cart_product.name
    
    def total_price(self):
        return format(self.quantity * self.cart_product.price,'0.2f')
    
class Order(models.Model):

    PAYMENT_METHOD = (
        ('Cash_On_Delivery','Cash On Delivery'),
        # ('SSLCommerz','SSLCommerz')
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_order")
    order_product = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=30,blank=True,null=True)
    order_id = models.CharField(max_length=30,blank=True,null=True)
    payment_method = models.CharField(max_length=30,choices=PAYMENT_METHOD,default="Cash_On_Delivery")
    created = models.DateTimeField(default=timezone.now)
    is_coupon = models.BooleanField(default=False)
    disconut_price = models.FloatField(default=0.0)

    def order_total_price(self):
        total = 0
        for item in self.order_product.all():
            total += float(item.total_price())
        return total
    


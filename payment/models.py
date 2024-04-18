from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class BillingAdress(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='payment_user')
    full_name=models.CharField(max_length=300)
    phone_number=models.CharField(max_length=300)
    email = models.EmailField(blank=True,null=True)
    city = models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    note=models.CharField(max_length=300)

class CouponCode(models.Model):
    coupon_code = models.CharField(max_length=300)
    discount_percent = models.IntegerField(default=0.0)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.coupon_code
    
class AppliedCouponCode(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='coupon_user')
    coupon = models.ForeignKey(CouponCode,on_delete=models.CASCADE, related_name='coupon_user')


    

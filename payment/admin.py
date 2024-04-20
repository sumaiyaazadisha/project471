from django.contrib import admin
from payment.models import BillingAdress,CouponCode,AppliedCouponCode
# Register your models here.
admin.site.register(BillingAdress)
admin.site.register(CouponCode)
admin.site.register(AppliedCouponCode)

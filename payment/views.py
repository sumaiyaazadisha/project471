from django.shortcuts import render,redirect
from payment.models import BillingAdress,CouponCode, AppliedCouponCode
from cart.models import Cart,Order
from django.utils import timezone
from django.contrib import messages
# Create your views here.

def checkout(request):
    save_address = BillingAdress.objects.get_or_create(user=request.user)
    address_obj = save_address[0]
    order_qs = Order.objects.filter(user=request.user,ordered=False)[0]
    cart_qs = Cart.objects.filter(user=request.user,purchased=False)
    
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        note = request.POST.get('note')

        address_obj.full_name = full_name
        address_obj.phone_number = phone
        # address_obj.email = email
        address_obj.address = address
        # address_obj.city = city
        # address_obj.note = note
        address_obj.save()

        if order_qs.payment_method == 'Cash_On_Delivery':
            order_qs.ordered = True
            order_qs.order_id = order_qs.id
            order_qs.save()

            for item in cart_qs:
                item.purchased = True
                item.save()
            messages.success(request,"Order confirm")
            return redirect("shop_product")   
    coupon = AppliedCouponCode.objects.filter(user=request.user)
    if coupon.exists():
        if order_qs.is_coupon == True:
            coupon = coupon[0]
        else:
            coupon= None

    context = {
        "address_obj":address_obj,
        "order":order_qs,
        "coupon":coupon,
    }

    return render(request,"payment/checkout.html",context)

def apply_coupon(request):
    if request.method == "POST":
        applied_coupon = request.POST.get('applied_coupon')
        coupon = CouponCode.objects.filter(coupon_code=applied_coupon,is_active=True)[0]
        order = Order.objects.filter(user=request.user,ordered=False,is_coupon=False)
        if order and coupon.end_date > timezone.now() :
            order = order[0]
            order.is_coupon = True
            coupon_discount_price = (int(order.order_total_price()) * coupon.discount_percent) / 100
            order.disconut_price = order.order_total_price() - coupon_discount_price
            order.save()
           
            AppliedCouponCode.objects.create(
                user=request.user,
                coupon = coupon
            )
    return redirect('checkout')
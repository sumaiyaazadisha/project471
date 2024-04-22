from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout



def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method=="POST":
        username= request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        pass1= request.POST["pass1"]
        pass2= request.POST["pass2"]
      

        if User.objects.filter(username=username):
            messages.error(request,"Username exists already! Try another one.")
            return redirect('home')
        
        if len(username)>8:
            messages.error(request, "Username must be 8 characters or less.")
            
        
        if pass1 != pass2:
            messages.error(request, "Invalid Password")
        
        
        if not username.isalnum():
            messages.error(request, "Username can only contain letters and numbers.")
            return redirect("home")


        myuser= User.objects.create_user(username, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Account has been successfully created!")
        return redirect('login')

    return render(request, "users/register.html")

def signin(request):
    if request.method == 'POST':
       username= request.POST['username']
       pass1= request.POST['pass1']

       user=authenticate(username=username, password=pass1)
       if user is not None:
            login(request, user)
            
            if user.is_superuser:
                return redirect('product')
            else:
                fname=user.first_name
                return render(request, "users/home.html", {'fname':fname})
            fname=user.first_name
            return redirect("shop_product")
       else:
            messages.error(request, "Bad Credentials")
            return redirect('home')



    return render(request, "users/login.html")

# def login(request):
#     if request.method == 'POST':
#        username= request.POST['username']
#        pass1= request.POST['pass1']

#        user=authenticate(username=username, password=pass1)
#        if user is not None:
#             login(request,user)
#             fname=user.first_name
#             return render(request, "users/home.html", {'fname':fname})
#        else:
#             messages.error(request, "Bad Credentials")
#             return redirect('home')

#     return render(request, "users/login.html")


#usertype
from cart.models import Order
@login_required()
def profile(request): 
    order_count = Order.objects.filter(user = request.user).count()
    context = {
        'order_count':order_count
    }
    return render(request, 'users/profile.html',context)



def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('login')

 #demoo pic in PC 
# def show(request):
#     return render(request, 'users/LOG.html')

##############################################################################################################

# from django.shortcuts import render
# from django.http import HttpResponse
# from testing.models import addData

# # Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.db import IntegrityError
from .models import Product,combo
from django.conf import settings
from django.db.models import Q


# def addQ(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         country = request.POST.get('country')
#         price = request.POST.get('price')

#         # Check if an object with the same name already exists
#         existing_object = addData.objects.filter(name=name).first()

#         if existing_object:
#             # Duplicate found, handle accordingly (e.g., display an error message)
#             return render(request, 'demo.html', {'message': 'Entry with this name already exists.'})

#         try:
#             # No duplicate found, save the new object
#             new_entry = addData(name=name, country=country, price=price)
#             new_entry.save()
#             return render(request, 'about.html', {'message': 'Entry added successfully.'})

#         except IntegrityError as e:
#             # Handle other integrity errors as needed
#             return render(request, 'demo.html', {'message': 'An error occurred: {}'.format(str(e))})

#     else:
#         # Handle GET requests or render the form
#         return render(request, 'about.html')

def tryf(request):
    return render(request, "test.html")
def demo(request):
    return render(request, "editproduct.html")

def trial(request):
    return render(request, "thankyou.html")


def edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'edit.html', {'product': product})

# Function to show the products(admin)
def product_list(request):
    order_by = request.GET.get('sort',None)

    if order_by == 'asc':
        products = Product.objects.all().order_by('rating')
    elif order_by == 'desc':
        products = Product.objects.all().order_by('-rating')
    # elif order_by == 'price':
    #     products = Product.objects.all().order_by('price')
    # elif order_by == 'price':
    #     products = Product.objects.all().order_by('price')
    else:
        products = Product.objects.all()

    return render(request, 'adminview.html', {'products': products})


# Function to show product in the webpage
def show_product(request, product_id):
    p = get_object_or_404(Product, pk=product_id)

    return render(request, 'product_view.html', {'p':p})


#SEARCH BOX
def product_list_shop(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        multiple_q = Q(Q(name__contains=searched) | Q(catagory__contains=searched) | Q(brand__contains=searched))
        products = Product.objects.filter(multiple_q)

    else:
        products = Product.objects.all()

    return render(request, 'shop.html', {'products': products})


# Function to add the products(admin)
def addProduct(request):
    n=''
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        catagory = request.POST.get('catagory')
        brand = request.POST.get('brand')
        country = request.POST.get('country')
        quantity = request.POST.get('quantity')
        rating = request.POST.get('rating')
        picture = request.FILES.get('picture')
        description = request.POST.get('description')

        # Save the data to the database
        Product.objects.create(
            name=name,
            price=price,
            catagory=catagory,
            brand=brand,
            country=country,
            quantity=quantity,
            rating = rating,
            img=picture,
            description=description
        )
        
        n="Added"
        return redirect('product') 
    

# Function to delete products(admin)   
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('product') 
   


# Function to update products(admin)
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        name = request.POST.get('name', product.name)
        price = request.POST.get('price', product.price)
        catagory = request.POST.get('catagory', product.catagory)
        brand = request.POST.get('brand', product.brand)
        country = request.POST.get('country', product.country)
        quantity = request.POST.get('quantity', product.quantity)
        date = request.POST.get('date', product.date)
        description = request.POST.get('description', product.description)

        picture = request.FILES.get('picture')

        # If no new picture is uploaded but there is an existing image in the database, keep it
        if not picture and product.img:
            picture = product.img

        # Update the product object
        product.name = name
        product.price = price
        product.catagory = catagory
        product.brand = brand
        product.country = country
        product.quantity = quantity
        product.date = date
        product.description = description

        # If a new picture is uploaded or there is an existing image, update the img field
        if picture:
            product.img = picture

        product.save()

        return redirect('product')





def p(request):
    # Retrieve all products from the database
    pro = Product.objects.all()

    # Pass the products to the template
    return render(request, 'addcombo.html', {'pro': pro})



# Function for adding combos (admin)
def add_combo(request):
    if request.method == 'POST':
        combo_name = request.POST.get('combo_name')
        product_names = request.POST.getlist('combo_products')
        combo_price = request.POST.get('combo_price')
        combo_img = request.FILES.get('picture')

        
        new_combo = combo.objects.create(combo_name=combo_name, combo_price=combo_price,combo_img=combo_img)
        
        # Adding products to the combo
        for product_name in product_names:
            product = Product.objects.get(name=product_name)
            new_combo.combo_products.add(product)
            
        
        return redirect('combo_detail')
    

#TOP 4 Products
# def top_product(request):
#     top_product = Product.objects.all()[:4]  # Assuming you want to show only 3 products
#     return render(request, 'product_view.html', {'top_product': top_product})


def see_combo(request):
    return render(request, "combo_view.html")



def combo_detail(request):
    combos = combo.objects.all()
    return render(request, 'combo_view.html', {'combos': combos})


 # Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,combo
from django.conf import settings
from django.db.models import Q
import csv
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed


def tryf(request):
    return render(request, "index.html")
def demo(request):
    return render(request, "editproduct.html")

def trial(request):
    return render(request, "findStype.html")


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

        duplicate = Product.objects.filter(
            name=name,
            brand=brand,
            catagory=catagory,
            country=country
        ).first()

        if duplicate:
            return redirect('addP')
        

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
    
    elif request.method == 'GET':
        return render(request, 'editproduct.html')

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
    

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
            
        
        return redirect('product')
    

#fetch all the combos
def combo_detail(request):
    combos = combo.objects.all()
    return render(request, 'combo_view.html', {'combos': combos})


def show_combo(request, combo_id):
    c = get_object_or_404(combo, pk=combo_id)

    return render(request, 'combo.html', {'c':c})


# Function to delete combo(admin)   
def delete_combo(request, combo_id):
    c = get_object_or_404(combo, pk=combo_id)
    c.delete()
    return redirect('product') 




#Finding skintype
def skin_quiz(request):
    result = None
    type=None
    context ={}
    
    if request.method == 'POST':
        score = 0
        
        # Question 1
        skin_feel = request.POST.get('skin_feel', None)
        if skin_feel:
            if skin_feel == 'dry':
                score += 1
            elif skin_feel == 'oily':
                score += 2
            elif skin_feel == 'combination':
                score += 1
        
        # Question 2
        shine = request.POST.get('shine', None)
        if shine:
            if shine == 'yes':
                score += 2
        
        # Question 3
        weather_condition = request.POST.get('weather_condition', None)
        if weather_condition:
            if weather_condition == 'dry':
                score += 1
            elif weather_condition == 'oily':
                score += 2
        
        # Question 4
        cleansing_feel = request.POST.get('cleansing_feel', None)
        if cleansing_feel:
            if cleansing_feel == 'tight':
                score += 1
            elif cleansing_feel == 'oily':
                score += 1
        
        # Question 5
        skin_texture = request.POST.get('skin_texture', None)
        if skin_texture:
            if skin_texture == 'rough':
                score += 1
            elif skin_texture == 'uneven':
                score += 2
        
        # Question 6
        moisturizer_feel = request.POST.get('moisturizer_feel', None)
        if moisturizer_feel:
            if moisturizer_feel == 'greasy':
                score += 1
            elif moisturizer_feel == 'still_dry':
                score += 2
        
        # Question 7
        morning_feel = request.POST.get('morning_feel', None)
        if morning_feel:
            if morning_feel == 'dull':
                score += 1
            elif morning_feel == 'oily':
                score += 2
        
        if score >= 12:
            result = 'Your skin type is Oily.'
            type= 'oily'
        elif score >= 10 and score <= 11:
            result = 'Your skin type is Combination.'
            type = 'combination'
        else:
            result = 'Your skin type is Dry.'
            type='dry'

        
        products = Product.objects.filter(catagory__icontains=type) 

        context = {
            'result': result,
            'products': products
        }
    
    
    
    return render(request, 'findStype.html', context)






#exporting to csv file function
def download_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)

    writer.writerow(['Image URL', 'Product Name', 'Price', 'Category', 'Brand', 'Rating', 'Quantity'])

    products = Product.objects.all()

    for product in products:
        writer.writerow([
            product.img.url,
            product.name,
            product.price,
            product.catagory,  
            product.brand,
            product.rating,
            product.quantity
        ])

    return response


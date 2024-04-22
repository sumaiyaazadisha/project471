from .models import combo,Product

def three_combos(request):
    three_combos = combo.objects.all()[:3]
    return {'three_combos': three_combos}


def top_products(request):
    top_products = Product.objects.order_by('-rating')[:3]
    return  {'top_products': top_products}


def combo_detail(request):
    combos = combo.objects.all()
    return  {'combos': combos}

def makeup_products_view(request):
    makeup_products = Product.objects.filter(catagory__icontains='makeup')[:3]
    return  {'makeup_products': makeup_products}

# def all_makeup(request):
#     products = Product.objects.all()
#     return  {'products': products}
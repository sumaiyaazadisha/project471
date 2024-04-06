from .models import combo,Product

def three_combos(request):
    # Retrieve any three combos
    three_combos = combo.objects.all()[:3]
    return {'three_combos': three_combos}


def top_products(request):
    # Retrieve the top three highest-rated products
    top_products = Product.objects.order_by('-rating')[:3]
    return  {'top_products': top_products}
from django.shortcuts import render

from product.models import Product


def index(request):
    products = Product.objects.filter(active=True)
    context = {
        'products':products
    }
    return render(request, 'index.html', context)
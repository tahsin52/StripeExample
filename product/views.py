from django.shortcuts import render

from product.models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
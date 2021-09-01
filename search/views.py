from django.shortcuts import render
from product.models import Product

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
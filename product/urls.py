from django.urls import path

from product.views import all_products

urlpatterns = [
    path('', all_products, name='products')
]
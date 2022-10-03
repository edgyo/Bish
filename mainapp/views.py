from sqlite3 import OperationalError
from django.shortcuts import render
from django.http import Http404

from .models import Product, ProductType

# Create your views here.

def home(request):
    return render(request, "home.html")

def shop(request):
    try:
        product_list = ProductType.objects.all()
        context = {
        'product_list': product_list,
    }
    except OperationalError:
        return Http404("No items currently available")
    return render(request, "shop.html", context)

def category(request, product_type):
    try:
        product_list = Product.objects.get_queryset().filter(type=product_type)
        context = {
        'product_list': product_list,
    }
    except OperationalError:
        return Http404("No items currently available")
    return render(request, "shop.html", context)
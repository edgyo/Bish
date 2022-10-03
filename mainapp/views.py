from sqlite3 import OperationalError
from django.shortcuts import render
from django.http import Http404

from .models import Product, ProductType

# Create your views here.

def home(request):
    return render(request, "home.html")

def shop(request):
    try:
        types_list = ProductType.objects.all()
        context = {
        'types_list': types_list,
    }
    except OperationalError:
        return Http404("No items currently available")
    return render(request, "shop.html", context)

def category(request, id):
    try:
        product_list = Product.objects.filter(type=id)
        type = ProductType.objects.get(id=id)
        context = {
        'product_list': product_list,
        'type':type,
        }
    except OperationalError:
        return Http404("No items currently available")
    return render(request, "category.html", context)
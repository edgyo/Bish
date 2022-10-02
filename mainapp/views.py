from django.shortcuts import render
from django.http import Http404

from .models import Product

# Create your views here.

def home(request):
    product_list = Product.objects.get_queryset()
    context = {
        'product_list': product_list,
    }
    return render(request, "home.html", context)
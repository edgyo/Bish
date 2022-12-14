from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='mainapp.home'),
    path('home', views.home, name='mainapp.home'),
    path('shop', views.shop, name='mainapp.shop'),
    path('shop/category=<int:id>', views.category, name='mainapp.category'),
]
from django.contrib import admin

from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ("name", "type", "price") # Fields to use for add/edit/show page
    list_display = ("name", "type", "price", "updated_at") # fields to display in search page

# Register app
admin.site.register(Product, ProductAdmin)
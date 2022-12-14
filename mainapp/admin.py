from django.contrib import admin

from .models import Product, Manufacturer, ProductType

# Register manufacturer
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("ru_name", "name")
admin.site.register(ProductType, ProductTypeAdmin)

# Make product rows clear-looking in admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "price", "manufacturer", "updated_at") # fields to display in search page

# Register product
admin.site.register(Product, ProductAdmin)

# Register manufacturer
admin.site.register(Manufacturer)
from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.name)

class ProductType(models.Model):
    name = models.CharField("Техническое название категории",max_length = 60)
    ru_name = models.CharField("Название",max_length = 60)
    image = models.ImageField(upload_to ='uploads/')

    def __str__(self):
        return(self.name)

class Product(models.Model):
    name = models.CharField(max_length = 120)
    price = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/')
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, default="unassigned")
    
    def __str__(self):
        return("{} ({})".format(self.name, self.type))
from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.name)
    
class Product(models.Model):
    name = models.CharField(max_length = 120)
    price = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/')

    TYPE_CHOICES = (
        ('Food', 'Food'),
        ('Drinks', 'Drinks'),
        ('Готовая еда', 'Готовая еда'),
        ('Фрукты', 'Фрукты'),
        ('Овощи', 'Овощи'),
        ('Напитки', 'Напитки'),
        ('Кофе', 'Кофе'),
    )

    type = models.CharField(choices=TYPE_CHOICES, max_length = 40)
    
    def __str__(self):
        return("{} ({})".format(self.name, self.type))
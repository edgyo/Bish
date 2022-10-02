from email.policy import default
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 120)
    price = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    TYPE = (
        ('Food', 'Food'),
        ('Drinks', 'Drinks'),
    )
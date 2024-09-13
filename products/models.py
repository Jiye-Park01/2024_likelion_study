from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30, blank=False, default='')
    price = models.DecimalField(max_digits=20, decimal_places=1,  blank=False, default=0)

class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    published_date = models.DateField()
    description = models.TextField()

from django.db import models
from datetime import datetime 

# Create your model  
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
    catagory = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    country = models.CharField(max_length=40)
    quantity = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    img = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

 
class combo(models.Model):
    combo_name = models.CharField(max_length=20)
    combo_products = models.ManyToManyField(Product)
    combo_price = models.IntegerField()
    combo_img = models.ImageField(upload_to='media/' ,default=None)

    def __str__(self):
        return self.combo_name



from django.db import models

from datetime import datetime 
from django.contrib.auth.models import User
from django.db.models import Avg, Count

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
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
    def category_preview(self):
        return self.catagory.split(',')[0] if ',' in self.catagory else self.catagory

    def skin_type(self):
        split_catagory = self.catagory.split(',', 1)

        if len(split_catagory) > 1:
            return split_catagory[1].strip()

        return 'Normal'

    
    def average_rating(self) -> float:
        return ProductRating.objects.filter(product=self).aggregate(Avg("rating"))["rating__avg"] or 0
    
    def total_rating(self) -> float:
        return ProductRating.objects.filter(product=self).aggregate(Count("rating"))["rating__count"] or 0
    
class ProductRating(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()

    def __str__(self):
        return f"Rating {self.rating} X {self.product.name}"

 
class combo(models.Model):
    combo_name = models.CharField(max_length=20)
    combo_products = models.ManyToManyField(Product)
    combo_price = models.IntegerField()
    combo_img = models.ImageField(upload_to='media/' ,default=None)

    def __str__(self):
        return self.combo_name
    
    def total_price(self):
        total_price = 0

        for product in self.combo_products.all():
            total_price += product.price

        return total_price
    
    def p_difference(self):
        total_price = self.total_price()

        price_difference =  total_price - self.combo_price 
 
        return price_difference



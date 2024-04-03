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
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=50,default="datetime.now()")

    def __str__(self):
        return self.name
    
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



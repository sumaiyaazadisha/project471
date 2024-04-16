from django.db import models


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
    
    def category_preview(self):
        """Returns the part of the category up to the first comma."""
        return self.catagory.split(',')[0] if ',' in self.catagory else self.catagory

    def skin_type(self):
        """Returns the part of the category after the first comma."""
        parts = self.catagory.split(',')
        return parts[1].strip() if len(parts) > 1 else ''

 
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



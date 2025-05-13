from django.db import models
# Create your models here.

# Category of product
class Category(models.Model):
    name = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name



# Product model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name 
    

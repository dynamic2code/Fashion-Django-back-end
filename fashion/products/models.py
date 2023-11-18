from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    details = models.TextField()
    preview_image_filename = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    count = models.IntegerField()
    preview_image_filename = models.CharField(max_length=255) 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_filename = models.CharField(max_length=255)  # Storing the filename as text

    def __str__(self):
        return f"Image for {self.product.name}"

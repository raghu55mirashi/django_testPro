from django.db import models

# Create your models here.


class Blog(models.Model):
    blog_id = models.AutoField
    blog_title = models.CharField(max_length=50)
    blog_desc = models.CharField(max_length=500)
    blog_date = models.DateField()


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='pics')
    product_avail = models.BooleanField(default=False)

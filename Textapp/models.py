from django.db import models

# Create your models here.

class category_db(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=50,null=True,blank=True)
    Cat_image = models.ImageField(upload_to="Category",null=True,blank=True)
class product_db(models.Model):
    Category_name = models.CharField(max_length=50,null=True,blank=True)
    Product_name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Brand = models.CharField(max_length=50, null=True, blank=True)
    Profile_img1 = models.ImageField(upload_to="Product_image",null=True,blank=True)
    Profile_img2 = models.ImageField(upload_to="Product_image",null=True,blank=True)
    Profile_img3 = models.ImageField(upload_to="Product_image",null=True,blank=True)



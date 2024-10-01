from django.db import models


# Create your models here.
class Contact_db(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email_Id = models.EmailField(max_length=50,null=True,blank=True)
    Message = models.TextField(max_length=50,null=True,blank=True)
class Sign_up(models.Model):
    Username = models.CharField(max_length=50,null=True,blank=True)
    Email_Id = models.EmailField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)
    Profile_image = models.ImageField(upload_to="Sign_up",null=True, blank=True)

class Cart_db(models.Model):
    User_Name = models.CharField(max_length=50,null=True,blank=True)
    Product_Name = models.CharField(max_length=50,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)

class Order_db(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Place = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=50, null=True, blank=True)
    Totalprice = models.IntegerField(null=True, blank=True)
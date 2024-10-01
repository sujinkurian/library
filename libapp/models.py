from django.db import models

# Create your models here.
class student_db(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Age = models.IntegerField(null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Address = models.CharField(max_length=50,null=True,blank=True)
    Course = models.CharField(max_length=50,null=True,blank=True)
    Gender = models.CharField(max_length=50,null=True,blank=True)
class book_db(models.Model):
    BookName = models.CharField(max_length=50,null=True,blank=True)
    Authorname = models.CharField(max_length=50,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Publishdate = models.DateField(null=True,blank=True)
class registraion_db(models.Model):
      Name = models.CharField(max_length=50,null=True,blank=True)
      Mobile = models.IntegerField(null=True, blank=True)
      Place = models.CharField(max_length=50, null=True, blank=True)
      Profileimage = models.ImageField(upload_to="Profile")

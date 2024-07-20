from django.db import models

# Create your models here.
class model1(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=15) 

class model2(models.Model):
    username = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 50)    

class model3(models.Model):
    name = models.CharField(max_length = 50)
    model = models.CharField(max_length = 50)
    price = models.IntegerField()
    quantity = models.IntegerField()

class cartmodel(models.Model):
    name = models.CharField(max_length = 50)
    model = models.CharField(max_length = 50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    email = models.EmailField(max_length = 100)
    phoneno = models.IntegerField() 
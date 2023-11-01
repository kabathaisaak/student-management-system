from django.db import models

# Create your models here.


class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.firstName + " " + self.lastName


class products(models.Model):
    productid = models.IntegerField(default=0)
    productname = models.CharField(max_length=50)
    productprice = models.IntegerField(default=0)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.productname



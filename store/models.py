from django.db import models

class Electronics(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()

class Apparel(models.Model):
    product_name = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    price = models.FloatField()

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField()
    genre = models.CharField(max_length=100)

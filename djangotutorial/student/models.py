from django.db import models

# Create your models here.
class student (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    file = models.FileField()
class product(models.Model):
     name = models.CharField(max_length=255, default='Unnamed Product')
     price = models.IntegerField(default=0)


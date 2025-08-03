from django.db import models

class File(models.Model):
    file = models.FileField(upload_to="files")

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)  
    gender = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)

from django.db import models
from django.contrib.auth.models import  User
from simple_history.models import HistoricalRecords
from django.utils import timezone

# Create your models here.
class Receipe(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True )
    receipe_name =  models.CharField(max_length=100)
    history = HistoricalRecords()
    receipe_description = models.TextField(blank=True)
    receipe_image = models.ImageField(upload_to='receipes', null=True, blank=True)
    recipe_count = models.IntegerField(default=1)

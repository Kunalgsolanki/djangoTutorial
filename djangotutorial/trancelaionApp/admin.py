from django.contrib import admin
from simple_history import register
from django.contrib.auth.models import User


register(User,  app=__package__)

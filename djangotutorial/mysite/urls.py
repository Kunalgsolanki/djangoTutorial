from django.contrib import admin
from django.urls import include, path
from vege.views import *

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("receipes/",receipes,name='receipes'),
    path("admin/", admin.site.urls),
]
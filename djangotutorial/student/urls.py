from django.urls import path
from .views import *

urlpatterns = [
    path('',get_home,name="student"),
    path('posttodo/',post_todo,name="post_todo")
]
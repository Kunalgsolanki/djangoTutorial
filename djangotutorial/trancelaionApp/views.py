from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext 
# Create your views here.
def index(request):
     
     return render(request,"trancelate.html")

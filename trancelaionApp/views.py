from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext 
from .models import Student
from django.http import HttpResponse,JsonResponse
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.
def index(request):
     
     return render(request,"trancelate.html")


def getStudent(request,pk):
     student = Student.objects.get(id =pk)
     serializer = StudentSerializer(student)
     jsonstudent = JSONRenderer().render(serializer.data)
     return JsonResponse(jsonstudent)


def getStudentlist(request):
     student = Student.objects.all()
     serializer = StudentSerializer(student,many=True)
     jsonstudent = JSONRenderer().render(serializer.data)
     return HttpResponse(jsonstudent,content_type="application/json")

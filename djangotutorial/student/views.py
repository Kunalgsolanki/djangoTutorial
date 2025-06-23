from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer

# Create your
#  views here.


@api_view(['GET', 'POST', 'PATCH'])
def get_home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message ': "yes Django Rest Freamwork is Working"
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message ': "yes Django Rest Freamwork is Working",
            'method_called':'Post Request',
            "data":request.data
        })
    elif request.method == 'PATCH':
        return Response({
            'status': 200,
            'message ': "yes Django Rest Freamwork is Working",
            'method_called':'PATCH Request',
            "data":request.data
        })
    else :
        return Response({
            'status': 404,
            'message ': "yes Django Rest Freamwork is Working",
            'method_called':'Invalid Request',
        })

@api_view(['POST'])
def post_todo (request):
    try:
        data = request.data 
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
           serializer.save() 
           print(serializer.data) 
           return Response({
            'status': True,
            'message ': "Success Data",
            'data':serializer.data
        } )
        else:
             return Response({
            'status': False,
            'message ': "Validation failed",
            'errors': serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
            'status': False,
            'message ': "Something Went Wrong",
        })

"""
 api view :
 api view is kind of decorator which not modified existing functionality of djnago function  or normal function modified 

 serilazer :
  convert data format to queryset to json .
"""
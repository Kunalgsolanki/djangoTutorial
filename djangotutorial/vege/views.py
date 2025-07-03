from django.shortcuts import render, redirect
from .models import Receipe
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


# Create Recipe Apis 
@login_required
def user_details(request):
    return render(request, "UserDetails.html")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
            user=request.user
        )
        return redirect("/receipes/")

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            receipe_name__icontains=request.GET.get('search'))
    context = {'receipes': queryset}
    return render(request, "receipes.html", context)


def delete_receipe(request, id):
    querySet = Receipe.objects.filter(id=id)
    querySet.delete()
    return redirect("/receipes/")


def update_receipe(request, id):
    querySet = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        querySet.receipe_name = receipe_name
        querySet.receipe_description = receipe_description

        if receipe_image:
            querySet.receipe_image = receipe_image

        querySet.save()
        return redirect("/receipes/")
    context = {'receipes': querySet}
    return render(request, "upadte_receipe.html", context)

def logout_page(request):
    logout(request)
    return redirect("/login/")
def login_page(request):    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(password)
        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username and password")
            return redirect('/login/')
        user =authenticate(username = username,password = password)

        if user is None:
            messages.error(request, "Invalid  password")
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect("/receipes/")

    return render(request, "login.html")


def register_page(request):

    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username") 
        password = data.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "UserName already taken")
            return redirect('/register/')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()

        messages.info(request,"Account Created Succesfully !")

        return redirect('/register/')
        
        

    return render(request, "register.html")

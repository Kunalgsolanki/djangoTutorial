from django.shortcuts import render, redirect
from .models import Receipe
from django.http import HttpResponse

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")
        
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        return redirect("/receipes/")  
    
    # For GET request
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains = request.GET.get('search'))
    context = {'receipes': queryset}
    return render(request, "receipes.html", context)
def delete_receipe(request,id):
    querySet = Receipe.objects.filter(id=id)
    querySet.delete()
    return redirect("/receipes/")
def update_receipe(request,id):
    querySet = Receipe.objects.get(id = id)
    
    if request.method =="POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        querySet.receipe_name = receipe_name
        querySet.receipe_description =receipe_description
        
        if receipe_image:
             querySet.receipe_image = receipe_image
    
    
        querySet.save()
        return redirect("/receipes/")
    context = {'receipes': querySet}
    return render(request,"upadte_receipe.html", context)

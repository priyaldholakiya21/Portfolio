from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    return render(request,"index.html",context)
def about(request):
    return HttpResponse("this is about page")
def services(request):
    return HttpResponse("this is services page")
def contact(request):
    return render(request,"contact.html")

from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),
        )
        return redirect("contact")  # reload page after submit

    return render(request, "contact.html")

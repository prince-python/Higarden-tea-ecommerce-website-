from django.shortcuts import render
from . models import *

def index(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')




def about(request):
    return render(request,'about.html')


def letstalk(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        msg=request.POST['msg']
        Contact.objects.create(name=name,msg=msg,subject=subject,email=email)
        return render(request,"contact.html")
    else:
        return render(request,"contact.html")
            
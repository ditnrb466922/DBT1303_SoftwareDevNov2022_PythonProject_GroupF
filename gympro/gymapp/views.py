from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from gymapp.models import gymdatabase


# Create your views here.
def home(request):
    return render(request,'index.html')

def enroll(request):
    if request.method=="POST":
    
        fname=request.POST['fname']
        gender=request.POST['gender']
        email=request.POST['email']
        phone=request.POST['phone']
        course=request.POST['course']
        room=request.POST['room']
        price=request.POST['price']
        

        register=gymdatabase(fname=fname,gender=gender,email=email,phone=phone,course=course,room=room,price=price)
        register.save()
        messages.success(request,"enrolled sucessfully.")
        
    return render(request,'enroll.html')

def room(request):

    rooz=gymdatabase.objects.filter(room__contains='roomz').values()
    rooy=gymdatabase.objects.filter(room__contains='roomy').values()
    roox=gymdatabase.objects.filter(room__contains='roomx').values()
    context={'roomz':rooz,'roomx':roox,'roomy':rooy}

    return render(request,'room.html',context)


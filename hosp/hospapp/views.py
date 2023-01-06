from django.shortcuts import render
from .models import Department,Doctors
from .forms import Bookingform 
# Create your views here.
def index(request):
    return render (request,'index.html')

def about(request):
   return render (request,'about.html')

def booking(request):
    if request.method=="POST":
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    formvb=Bookingform()
    dict_book={
        'book':formvb
    }
     
    return render (request,'booking.html',dict_book)

def contact(request):
    return render (request,'contact.html')

def docters(request):
    dict_doc={
        'doc':Doctors.objects.all()
    }

    return render (request,'docters.html',dict_doc)

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render (request,'department.html',dict_dept)

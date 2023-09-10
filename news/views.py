from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        age=request.POST['age']
        Person(name=name, address=address, age=age).save()
    return render(request, "index.html")

def send(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        age=request.POST['age']
        Person(name=name, address=address, age=age).save()
    return render(request, 'index.html')

def show(request):
    data=Person.objects.all()
    return render(request, 'show.html', {'data':data})

def delete(request):
    id=request.GET['id']
    Person.objects.filter(id=id).delete()
    return HttpResponseRedirect("show")

def edit(request):
    id=request.GET['id']
    name=address=age="Not Availabel"
    for data in Person.objects.filter(id=id):
        name=data.name
        address=data.address
        age=data.age
    
    return render(request, 'edit.html',{'name':name, 'address':address, 'age':age})

def record(request):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        age=request.POST['age']
        Person.objects.filter(name=name).update(address=address, age=age)
    return HttpResponseRedirect("show")

def person(request):
    return render(request, 'person/person.html')

def hobby(request):
    return render(request, 'hobby/hobby.html')

def forms(request):
    return render(request, 'forms.html')

def cv(request):
    return render(request, 'CV/cv.html')

def cv_show(request):
    return render(request, 'CV/cv_show.html')    
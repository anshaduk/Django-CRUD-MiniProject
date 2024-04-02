from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
    data=Student.objects.all()
    context={'data':data}
    return render(request,'index.html',context)

def insertData(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        print(name,email,password,gender)
        query=Student(name=name,email=email,password=password,gender=gender)
        query.save()
        return redirect("/")
    return render(request,'index.html')


def updateData(request,id):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        gender=request.POST['gender']
        
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.password=password
        edit.gender=gender
        edit.save()
        return redirect("/")
    d=Student.objects.get(id=id)
    context={'d':d}
    return render(request,'update.html',context)

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    
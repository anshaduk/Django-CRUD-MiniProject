from django.shortcuts import render
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
        
    return render(request,'index.html')

from django.shortcuts import  render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def aboutMe(request):
    return render(request,'aboutMe.html')

def contact(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'projects.html')
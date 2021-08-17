from django.shortcuts import render, HttpResponse, redirect
from .models import *
#  User
from django.contrib import messages

def log_and_reg(request):
    return render(request, "log_and_reg.html")

def index(request):
    return HttpResponse("This is my response")

def detail(request):
    message = "Hello"
    return HttpResponse(message)

def home(request):
    return render(request, "home.html")

def dashboard(request):
    return render(request, "dashboard.html")    

def job(request):
    return render(request, "job.html")

def edit(request):
    return render(request, "edit.html") 

def wish(request):
    return render(request, "wish.html") 

def view(request):
    return render(request, "view.html")     
    


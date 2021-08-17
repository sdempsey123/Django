from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is my response")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request):
    return HttpResponse("placeholder to display blog number 15")

def person(request, name):
    return HttpResponse("Hello")

def edit(request):
    return HttpResponse("placeholder to edit blog {number}")

def steve(request, number):
    return HttpResponse("15")

def destroy(request):
    return redirect("/")


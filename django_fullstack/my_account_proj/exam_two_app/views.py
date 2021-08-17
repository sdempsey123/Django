from django.shortcuts import render, redirect 
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return HttpResponse("This is my response")

def log_and_reg(request):
    return render(request, "index.html")

def logout(request):
    request.session.flush()
    return redirect("/")
        

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
    if user: 
        logged_user = user[0]
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        request.session[user_id] = logged_user.id
        messages.success(request, "Successfully logged in")
        return redirect("/shows")
        messages.error(request, "Password does not match")
    else:
        messages.error(request, "Email does not exist")

    return redirect ('/')


def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash
            )   
            request.session['user_id'] = user.id
            messages.success(request, "Successfully registered")
            return redirect("/success")
    return redirect("/")
        
           

def shows(request):
    if not 'user_id' in request.session:
        return redirect("/")
    context = {
        "shows": Show.objects.all(),
        "user": User.objects.get(id=request.session[user_id])
    }
    return render(request, "index.html", context)

def success(request):
    if not 'user_id' in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "index.html", context)
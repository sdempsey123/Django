from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User, MessagePost

def log_and_reg(request):
    return render(request, "register.html")

def register(request, id):
    errors = Register.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        register = Register.objects.get(id = id)
        register.first_name = request.POST['first_name']
        register.last_name = request.POST['last_name']
        register.email = request.POST['email']
        register.password = request.POST['password']
        register.save()
        messages.success(request, "Register successfully updated")
        return redirect('/')



def login(request, id):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
    if user: 
        logged_user = user[0]
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        request.session[user_id] = logged_user.id
        messages.success(request, "Successfully logged in")
        return redirect("/")
        messages.error(request, "Password does not match")
    else:
        messages.error(request, "Email does not exist")

    return redirect ('/')

def success(request):
    if not 'user_id' in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['user_id'])
        # 'all messages':MessagePost.objects.all()
    }
    return render(request, "success.html", context) 

def create_mess(request):
    if request.method=='POST':
        error=MessagePost.objects.empty_validator(request.POST)
        if error:
            messages.error(request, error)
            return redirect('/success')
        MessagePost.objects.create(content=request.POST['content'], poster=User.objects.get(id=request.session['user.id']))
        return redirect('/')

        MessagePost.objects.create(content=request.POST['content'], poster=User.objects.get(id=request.session['user_id']))
        return redirect('/success')
    return redirect('/')








# Create your views here.

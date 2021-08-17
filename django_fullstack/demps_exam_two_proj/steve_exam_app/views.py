from django.shortcuts import render, HttpResponse, redirect
from .models import *
#  User
from django.contrib import messages
import bcrypt


# Create your views here.
def detail(request):
    message = "Hello"
    return HttpResponse(message)

def log_and_reg(request):
    return render(request, "log_and_reg.html")

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        user = User.objects.filter(email=request.POST['email']) # why are we using filter here instead of get?
        if user: # note that we take advantage of truthiness here: an empty list will return false
            logged_user = user[0] 
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['userid'] = logged_user.id
            messages.success(request, "Successfully created account")
            return redirect("/home")
            messages.errors(request, "Invalid Email/Password combo")
        else:
            messages.error(request, "Account with email not found")
            # never render on a post, always redirect!
            
    return redirect("/") 

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        print(pw_hash)      # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
        # be sure you set up your database so it can store password hashes this long (60 characters)
        # make sure you put the hashed password in the database, not the one from the form!
        user = User.objects.create(email=request.POST['email'], password=pw_hash) 
        request.session['userid'] = user.id
        messages.success(request, "Successfully registered!")
        return redirect("/home")


    return redirect("/")

def home(request):
    # if not 'userid' in request.session:
    #     return redirect("/")
        # else:   
    #     context ={
    #         "user": User.objects.get(id=request.session['userid'])
    #     }
    return render(request, "home.html") 

def logout(request):
    request.session.flush()
    return redirect("/")

def wishes(request):
    # if not 'userid' in request.session:
    #     return redirect("/")
    # else:   
    #     context ={
    #         "user": User.objects.get(id=request.session['userid'])
            
            
    #     }
        return render(request, "wishes.html") 
    
def new(request):
    # if not 'userid' in request.session:
    #     return redirect("/")
    # else:   
        # context ={
        #     "user": User.objects.get(id=request.session['userid'])
        # }
        return render(request, "new.html") 

def edit(request):
    # if not 'userid' in request.session:
    #     return redirect("/")
    # else:   
    #     context ={
    #         "user": User.objects.get(id=request.session['userid'])
    #     }
    return render(request, "edit.html")

def stats(request):
    # if not 'userid' in request.session:
    #     return redirect("/")
    # else:   
    #     context ={
    #         "user": User.objects.get(id=request.session['userid'])
    #     }
    return render(request, "stats.html") 

def new_wish(request):
    if request.method == 'POST':
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/new')
        else:
            Wish.objects.create(item=request.POST['item'], desc=request.POST['desc'], user=User.objects.get(id=request.POST['user_id']))
            return redirect('/wishes')
    else:
        return redirect('/')

def grant(request):
    if request.method == 'POST':
        Granted_wish.objects.create(item=request.POST['wish_item'], user=User.objects.get(id=request.POST['user_id']), date_added=request.POST['wish_created'])
        wish = Wish.objects.get(id=request.POST['wish_id'])
        wish.delete()
        return redirect('/wishes')
    else:
        return redirect('/')

def update(request, id):
    if request.method == 'POST':
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/edit')
        else:
            wish = Wish.objects.get(id= id)
            wish.item = request.POST['item']
            wish.desc = request.POST['desc']
            wish.save()
            return redirect('/wishes')    
    else:
        return redirect('/')

def like(request):
    if request.method == 'POST':
        granted = Granted_wish.objects.get(id=request.POST['grant_id'])
        user = User.objects.get(id=request.POST['user_id'])
        if granted.user_id == user.id:
            messages.error(request, "Users may not like their own wishes.")
            return redirect('/wishes')
        if len(granted.likes.filter(id=request.POST['user_id'])) > 0:
            messages.error(request, "You have already liked this wish.")
            return redirect('/wishes')
        else:
            granted.likes.add(user)
            return redirect('/wishes')

def delete(request):
    if request.method == 'POST':
        wish = Wish.objects.get(id=request.POST['wish_id'])
        wish.delete()
        return redirect('/wishes')
    else:
        return redirect('/')              


     
    

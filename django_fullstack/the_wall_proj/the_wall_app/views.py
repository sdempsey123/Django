from django.shortcuts import render, redirect 
from .models import Comment, User, Wall_Message
from django.contrib import messages
import bcrypt



# Create your views here.
def log_and_reg(request):
    return render(request, "the_wall.html")



def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
    if user: 
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session["user_id"] = logged_user.id
            messages.success(request, "Successfully logged in")
            return redirect ('/wall')
        else:
            messages.error(request, "Email does not exist")
            return redirect ('/wall')
    

def logout(request):
    request.session.flush()
    return redirect("/")
        # if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()
        #   request.session['user_id'] = logged_user.id  
        # return redirect('/success') 
        # return redirect("/")   


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
            return redirect("/wall")
    return redirect("/")
        
           

# def shows(request):
#     if not 'user_id' in request.session:
#         return redirect("/")
#     context = {
#         "shows": Show.objects.all(),
#         "user": User.objects.get(id=request.session[user_id])
#     }
#     return render(request, "the_wall.html", context)

def wall(request):
    if not 'user_id' in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "wall_messages": Wall_Message.objects.all()
    }
    return render(request, "message.html", context)

def post_message(request):
    if request.method == "POST":
        errors = Wall_Message.objects.message_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect("/wall")
        else:
            Wall_Message.objects.create(message=request.POST['message'], poster=User.objects.get(id=request.session['user_id']))
            return redirect("/wall")

# def message(request):
#     context = {"wall_messages": Wall_Message.objects.all()}
#     return render(request, "message.html", context)

def post_comment(request):
    if request.method == "POST":
        errors = comment.objects.comment_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                comments.error(request, value)
                return redirect("/wall")
        else:
            Wall_Comment.objects.create(comment=request.POST['comment'], poster=User.objects.get(id=request.session['user_id']))
            return redirect("/wall")
            
    return redirect("/wall")

def delete_message(request, wall_message_id):
    if request.method == "POST":
        wall_message = Wall_Message.objects.get(id=comment_id)
        wall_message.delete()

        return redirect("/wall")

def delete_comment(request, comment_id):
    if request.method == "POST":
        # if comment.poster.id == request.session(['user_id'])
            comment = Comment.objects.get(id=comment_id)
            comment.delete()

            return redirect("/wall")
        
def profile(request, profile_id):
    user = User.objects.get(id=profile_id)
    context = {
        "user": User.objects.get(id=profile_id)
    } 
    return render(request, "profile.html", context)
    



    
from django.shortcuts import render, redirect
from .models import Show
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def log_and_reg(request):
        return render(request, "log_and_reg.html")

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'log_and_reg.html', context)



def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/shows')

def new(request):
    return render(request, 'new.html')

# def login(request):
#     if request.method == "GET":
#         return redirect('/')
#     if not User.objects.authenticate(request.POST['email'], request.POST['password']):
#         messages.error(request, 'Invalid Email/Password')
#         return redirect('/')
#     user = User.objects.get(email=request.POST['email'])
#     request.session['user_id'] = user.id
#     messages.success(request, "You have successfully logged in!")
#     return redirect('/success')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
    if user: 
        logged_user = user[0]
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        request.session['user_id'] = logged_user.id
        messages.success(request, "Successfully logged in")
        return redirect("/shows")
        # messages.error(request, "Password does not match")
    else:
        messages.error(request, "Email does not exist")

    return redirect ('/')






def logout(request):
        request.session.clear()
        return redirect("/")
            


def create(request):
    #CREATE THE SHOW
    errors = Show.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    
    Show.objects.create(
            destination = request.POST['destination'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            plan = request.POST['plan']

    )
   
    return redirect('/shows')

def edit(request, show_id):
        one_show = Show.objects.get(id=show_id)
        context = {
            'show': one_show
        }
        return render(request, 'edit.html', context)

def update(request, show_id):
    # update show!
    to_update = Show.objects.get(id=show_id)
    # updates each field
    to_update.destination = request.POST['destination']
    to_update.start_date = request.POST['start_date']
    to_update.end_date = request.POST['end_date']
    to_update.plan = request.POST['plan']
    to_update.save()

    return redirect('/shows/')




def show(request, show_id):
#     #query for one show with show_id
    # if 'user_id' not in request.session:
    #     return redirect('/')
    # user = User.objects.get(id=request.session['user_id'])
    one_show = Show.objects.get(id=show_id)
    #access all shows, set to variable
    context = {
        # 'user': user,
        'show': one_show
        #all shows variable
}
    return render(request, 'shows.html', context)

def delete(request, show_id):
    
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')

def shows(request):
    return render(request, 'shows.html')




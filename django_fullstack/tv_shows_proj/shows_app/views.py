from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .models import Show

# Create your views here.

def log_and_reg(request):
        return render(request, "log_and_reg.html")

# def index(request):
#    return render(request, 'log_and_reg.html')

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)



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

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/shows')

def logout(request):
    request.session.clear()
    return redirect('/')

def new(request):
    return render(request, 'new.html')

def create(request):
    # CREATE THE SHOW
    errors = Show.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        # description = request.POST['description']
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
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect('/shows/')

def show(request, show_id):
    # query for one show with show_id
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    # NOTE: Delete one show!
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')

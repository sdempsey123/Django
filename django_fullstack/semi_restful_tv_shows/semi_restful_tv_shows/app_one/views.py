from django.shortcuts import render, redirect
from.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "index.html", context)

def create_show(request):
    if request.method == "POST":
        errors = Show.objects.create_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
        # else:   
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    ) 
    return redirect('/')

def show_show(request, show_id):
    context = {
        'one_show': Show.objects.get(id=show_id)
    }
    return render(request, "one_show.html", context)        

def delete_show(request, show_id):
    if request.method == "POST":
        show_to_delete = Show.objects.get(id=show_id)
        show_to_delete.delete()
    return redirect('/')

def edit_show(request, show_id):
    context = {
        'one_show': Show.object.get(id=show_id)
    }
    return render(request, "edit_show.html", context) 

def update_show(request, show_id):    
   if request.method == "POST":
    errors = Show.objects.edit_validator(request.POST, show_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'shows/{show_id}/edit')
        # else:   
    show = Show.objects.get(id=show_id)
    show.title = request.POST['show_title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f'/shows/{show_id}')


        # title = request.POST['title'],
        # network = request.POST['network'],
        # release_date = request.POST['release_date'],
        # description = request.POST['description']
    # ) 
    return redirect('/')     
        # show = Show.objects.create(title request.POST['title'], network request.POST['network'], release_date request.POST['request_date'], description request.POST['description']) 
    
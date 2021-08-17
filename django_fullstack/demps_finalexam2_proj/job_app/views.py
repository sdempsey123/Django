from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job
from .models import User

# Create your views here.
def log_and_reg(request):
        return render(request, "log_and_reg.html")

def index(request):
    return render(request, 'log_and_reg.html')



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
        return redirect('/jobs')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/dashboard')

def create(request):
    # CREATE THE SHOW
    errors = Job.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/jobs/new')

    Job.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        location = request.POST['location'],
        
    )
    return redirect('/edit')

def edit(request):
    # one_show = Job.objects.get(id=job_id)
    # context = {
    #     'job': one_job
    # }
    return render(request, 'edit.html')

def new(request):
    return render(request, 'new.html')

# def jobs(request, job_id):
    
#     one_show = Job.objects.get(id=job_id)
#     context = {
#         'job': one_job
#     }
#     return render(request, 'jobs.html', context)

def jobs(request):
    return render(request, 'jobs.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def update(request, job_id):
        # update show!
        to_update = job_id.objects.get(id=job_id)
        # updates each field
        to_update.title = request.POST['title']
        to_update.description = request.POST['description']
        to_update.location = request.POST['location']
        to_update.save()

        # return redirect('/dashboard')
        redirect('update_user', job_id)
from django.shortcuts import render, redirect
from time import gmtime, strftime
from datetime import datetime
    
# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "other_time": datetime.now()
    }
    return render(request,'index.html', context)

def home(request):
    return redirect('/')

# Run this in terminal
# >>> datetime.datetime.now()
# datetime.datetime(2021, 4, 12, 11, 55, 53, 356870)
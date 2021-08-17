from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render
from time import gmtime, strftime


# def home_page(request):
#     print("I AM RESPONDING TO A URL REQUEST USING DJANGO")
#     return render("home.html")

# def python_page(request):
#     print("I HAVE SENT A REQUEST TO THE PYTHON PAGE")
#     return render(request, "python.html")


def form_index(request):
    if request.method == "POST":
        print("POST request")

    languages = request.POST.getlist("language")

    context = {
        "name": request.POST["name"],
        "location": request.POST.get["location"],
        "languages": languages,
        "comment": request.POST["comment"]
    }     
def index(request):
    return render(reqeust, 'survey.html', context)  
        





def index(request):
    today = date.today()
    print(today)


    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        'todaydate': today
    }
    return render(request,'home.html', context)
    



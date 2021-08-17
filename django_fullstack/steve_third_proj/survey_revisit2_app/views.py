from django.shortcuts import render, redirect, HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
    
def result(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        if not "prev_name" in request.session:
            request.session['prev_name'] = "Bob"
            context = {
                "name": request.POST["name"],
                "location": request.POST["location"],
                "language": request.POST["language"],
                "comment": request.POST["comment"],
                "prev_name": request.session['prev_name']
            }
    request.session['prev_name'] = request.POST["name"]
    return render(request, 'result.html', context)
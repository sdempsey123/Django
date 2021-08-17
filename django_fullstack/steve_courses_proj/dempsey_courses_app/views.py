from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
	context = {
        'courses': Course.objects.all()
    }
	return render(request, 'index.html', context)

# def delete(request, courseid):
#     to_delete = Course.objects.get(id=courseid)
#     to_delete.delete()
#     return render(request, 'delete.html')
	
def delete(request):
	context = {
	"courses": Course.objects.all()
	}
	
	return render(request, "delete.html", context)

def add(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.items():
			messages.error(request, error, extra_tags=tag)
		return redirect("/")
	else:
		coursename = request.POST['name']
		coursedesc = request.POST['desc']
		Course.objects.create(name = coursename, desc=coursedesc)
		createCourse()
		return redirect("/")


def destroy(request, id):
		courseid = request.POST['id']
		c = Course.objects.get(id=courseid)
		c.delete()
		return redirect("/")

def comments(request, id):
	context = {
		"comments": Comment.objects.filter(course = Course.objects.filter(id=id))
	}
	return render(request, "comments.html", context)

def comment(request):
		comment = request.POST['comment']
		courseid = request.POST['id']
		createdcomment = Comment.objects.create(comment= comment)
		createdcomment.course= courseid
		createdcomment.save()
		return redirect("/comments/"+courseid)

# ------------------------------------------------------------------------------------------------------------------

# def index(request):
#     context = {
#         'courses': Course.objects.all()
#     }
#     return render(request, 'index.html', context)

# def new(request):
#     return render(request, 'new.html')

# def create(request):
#     #CREATE THE SHOW
#     Show.objects.create(
#         title = request.POST['title'],
#         network = request.POST['network'],
#         release_date = request.POST['release_date'],
#         description = request.POST['description']
#     )
#     return redirect('/shows')

# def edit(request, show_id):
#     one_show = Show.objects.get(id=show_id)
#     context = {
#         'show': one_show
#     }
#     return render(request, 'edit.html', context)

# def update(request, show_id):
#     #update show!
#     to_update = Show.objects.get(id=show_id)
#     #updates each field
#     to_update.title = request.POST['title']
#     to_update.release_date = request.POST['release_date']
#     to_update.network = request.POST['network']
#     to_update.description = request.POST['description']
#     to_update.save()

#     return redirect('/shows')

# def show(request, show_id):
#     #query for one show with show_id
#     one_show = Show.objects.get(id=show_id)
#     context = {
#     'show': one_show
#     }
#     return render(request, 'show.html', context)

# def delete(request, show_id):
#     
#     to_delete = Course.objects.get(id=course_id)
#     to_delete.delete()
#     return render(request, 'new.html')
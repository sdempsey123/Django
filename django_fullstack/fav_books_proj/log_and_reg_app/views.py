from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt



# Create your views here.
def log_and_reg(request):
        return render(request, "log_and_reg.html")

def register(request):
    # if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            
            print("No errors found")
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash
            )   
            request.session['user_id'] = user.id
            # messages.success(request, "Successfully registered")
            # return redirect("/success")
        return redirect('/books')

def books(request):
        if 'user_id' in request.session:
            context = {
                'user': User.objects.get(id=request.session['user_id']),
                'all_books': Book.objects.all()
        }
            return render(request, 'books.html', context)
        return redirect('/')
        



def logout(request):
        request.session.flush()
        return redirect("/")
            # if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()
            #   request.session['user_id'] = logged_user.id  
            # return redirect('/success') 
            # return redirect("/")   

def login(request):
    # if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user: 
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session[user_id] = logged_user.id
        # messages.success(request, "Successfully logged in")
        return redirect("/books")
    #     messages.error(request, "Password does not match")
    # else:
        messages.error(request, "Email does not exist")
        return redirect ('/')
    
def create(request):
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books') 
        else:
                
            user = User.objects.get(id=request.session['user_id'])
            book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            uploaded_by = user
        )
            user.liked_books.add(book)
            
        return redirect('/books')

def book_profile(request, book_id):
        if 'user_id' in request.session:
            context = {
                'user': User.objects.get(id=request.session['user_id']),
                'all_books': Book.objects.get(id=book_id)
            }
            return render(request, 'book_profile.html', context)
        return redirect('/') 

def update(request, book_id):
        if 'user_id' in request.session:
            book = Book.objects.get(id=book_id)
            book.description = request.POST['description']
            book.save()
            return redirect(f"/books/{book_id}")
        return redirect('/') 

def delete(request, book_id):
        if 'user_id' in request.session:
            book = Book.objects.get(id=book_id)
        book.delete()
        return redirect(f"/books")
        return redirect('/') 

def unfavorite(request, book_id):
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id'])
            book = Book.objects.get(id=book_id)
            user.liked_books.remove(book)
            
            return redirect(f"/books/{book_id}")
        return redirect('/') 

def favorite(request, book_id):
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id'])
            book = Book.objects.get(id=book_id)
            user.liked_books.add(book)
            
            return redirect(f"/books/{book_id}")
        return redirect('/') 







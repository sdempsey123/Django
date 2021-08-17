from django.db import models
from datetime import datetime
import re
import bcrypt
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'

        if len(form['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'
        
        email_check = self.filter(email=form['email'])
        if email_check:
            errors['email'] = "Email already in use"

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        
        return errors
    
    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            password = pw,
        )
        
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()

class ShowManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        if len(post_data['destination']) < 2:
            errors["destination"] = "Destination must be at least 2 characters"
        if len(post_data['start_date']) < 2:
            errors["start_date"] = "Start date must be at least 2 characters"
        if len(post_data['end_date']) < 2:
            errors["end_date"] = "Description must be at least 2 characters"
        if len(post_data['plan']) < 2:
            errors["plan"] = "Plan must be at least 2 characters"

        
        
        return errors


class Show(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    plan = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

# class NewManager(models.Manager):
#     def basic_validator(self, post_data):
#         errors = {}
#         if len(post_data['destination']) < 3:
#             errors["destination"] = "Destination must be at least 3 characters"
#         if len(post_data['plan']) < 2:
#             errors["start_date"] = "Plans must be at least 2 characters"

    

# class New(models.Model):
#     destination = models.CharField(max_length=255)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     plan = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     objects = NewManager()



   
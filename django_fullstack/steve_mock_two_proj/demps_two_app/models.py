from django.db import models
from django.contrib.auth.models import User
import re

# Create your models here.
class RegisterManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if len(postData['password']) < 2:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] == postData['confirm_password']:
            errors['confirm_password'] = "Passwords must match"           
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
            return errors    

class Register(models.Model):
    first_name = models.CharField(max_length=255)
    last_mame = models.CharField(max_length=255)
    email = models.CharField(max_length=45)
    # password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    objects = RegisterManager()

class MessageManager(models.Manager):
    def empty_validator(self, postData):
        errors=""
        if len(postData['content']) < 1:
            errors="You must provide content to your Post"
            
        return errors

class MessagePost(models.Model):
    content=models.TextField()
    poster=models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=MessageManager()

class Book(models.Model):
    title=models.CharField(max_length=255) 
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=BookManager()


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_mame = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


from django.db import models

# Create your models here.
from django.db import models
    
class UserManager(models.Manager):
    def login_validator(self, post_dictionary):
        errors = {}
        if len(post_dictionary["email"]) <3:
            errors['email'] = "Email needs to be 3 characters"
        if len(post_dictionary["password"]) <3:
            errors['password'] = "Password needs to be 3 characters"
        return errors

    def register_validator(self, post_dictionary):
        errors = {}
        if len(post_dictionary["first_name"]) <3:
            errors['first_name'] = "First name needs to be 3 characters"
        if len(post_dictionary["last_name"]) <3:
            errors['last_name'] = "Last name needs to be 3 characters"
        if len(post_dictionary["email"]) <3:
            errors['email'] = "Email needs to be 3 characters"
        if len(post_dictionary["password"]) <3:
            errors['password'] = "Password needs to be 3 characters"
        if post_dictionary['password'] != post_dictionary['confirm_password']:
            errors['confirm_PW'] = "Passwords must match!"
        return errors  
        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class WishManager(models.Manager):
    def wish_validator(self, post_dictionary):
        errors = {}
        if len(post_dictionary["item"]) <3:
            errors['item'] = "Item needs to be 3 characters"
        if len(post_dictionary["desc"]) <3:
            errors['description'] = "Description needs to be 3 characters"
        return errors

class Wish(models.Model):
    item = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()

class Granted(models.Model):
    item = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    granted_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    


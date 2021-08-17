from django.db import models
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


       
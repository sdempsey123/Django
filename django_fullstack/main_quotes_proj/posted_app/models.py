from django.db import models
import re
# Create your models here.

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if len(postData['password']) < 2:
            errors['password'] = "Password must be at least 8 characters"    
        if postData['password'] == postData['confirm_password']:
            errors['confirm_pw'] = "Passwords must match"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
            return errors


class Author(models.Model):
    author = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quote(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData)['author'] > 3:
            errors['author'] = "Author name must be more than 3 characters"
        if len(postData)['quote'] > 10:
            errors['quote'] = "Quote must be more than 10 characters"
          
    
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class MessageManager(models.Manager):
    def message_validator(self, postData):
        errors = {}
        if len(postData)['message'] < 1:
            errors["message"] = "Wall Message must be at least 1 character"
    
        return errors

class Wall_Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="user_messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if len(postData)['comment'] < 1:
            errors["message"] = "Comment must be at least 1 character"
    
        return errors    

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    wall_message = models.ForeignKey(Wall_Message, related_name="wall_message_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()   
# Create your models here.

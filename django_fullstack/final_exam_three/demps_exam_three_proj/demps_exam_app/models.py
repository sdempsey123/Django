from django.db import models

# Create your models here.


# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class JobManager(models.Manager):
    def job_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) > 3:
            errors["title"] = "Title name should be at least 3 characters"
        if len(postData['desc']) > 10:
            errors["desc"] = "Description should be at least 10 characters"
        if len(postData['location']):
            errors["location"] = "Location must not be blank"
        return errors



class Job(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = JobManager()

class EditManager(models.Manager):
    def edit_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) > 3:
            errors["title"] = "Title name should be at least 3 characters"
        if len(postData['desc']) > 10:
            errors["desc"] = "Description should be at least 10 characters"
        if len(postData['location']):
            errors["location"] = "Location must not be blank"
        return errors

class Edit(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = EditManager()
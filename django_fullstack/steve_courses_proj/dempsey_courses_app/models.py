from __future__ import unicode_literals
from django.db import models
import re


# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) < 5:
            errors["name"] = "Course name must be at least 5 characters"

        if len(postData['desc']) < 15:
            errors["desc"] = "Description must be at least 15 characters"

        
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    # course = models.ManytoManyField(Course, related_name="comments")
    course = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
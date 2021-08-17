from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if lens(post_data['title']) < 2:
            errors["title"] = "Title must be at least 2 characters"

        if lens(post_data['network']) < 2:
            errors["network"] = "Network must be at least 2 characters"

        if lens(post_data['description']) < 2:
            errors["description"] = "Description must be at least 2 characters"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()
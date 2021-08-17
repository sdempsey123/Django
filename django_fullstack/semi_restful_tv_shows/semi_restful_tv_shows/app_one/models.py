from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        shows_with_name = Chicken.objects.filter(name=reqPOST['show_name'])
        if len(shows_with_name) >= 1:
            errors['unique'] = "Show already taken"
        if len(reqPOST['show_title']) < 3:
            errors['name'] = "Name is too short, use at least 3 characters"
            if len(reqPOST['network']) < 3:
                errors['network'] = "Network is too short, use at least 3 characters"
        return errors

def edit_validator(self, reqPOST, show_id):
        errors = {}
        shows_with_name = Chicken.objects.filter(name=reqPOST['show_name'])
        if len(shows_with_name) >= 1:
            if show_id != shows_with_title[0].id:
                errors['unique'] = "Show already taken"
        if len(reqPOST['show_title']) < 3:
            errors['name'] = "Name is too short, use at least 3 characters"
            if len(reqPOST['network']) < 3:
                errors['network'] = "Network is too short, use at least 3 characters"
        return errors

class Show(models.Model):
            title = models.CharField(max_length=50)
            network = models.CharField(max_length=50)
            release_date = models.DateField()
            description = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
            objects = ShowManager()

def __repr__(self):
			return f"<Show object: {self.title} ({self.network})>"		
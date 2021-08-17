from django.db import models


# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # MIGRATE AND MIGRATE AGAIN IF I MAKE CHANGES

    def __repr__(self):
        return f"<User object: {self.first_name} ({self.id})>"
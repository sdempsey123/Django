from django.db import models

# Create your models here.
class dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # MIGRATE AND MIGRATE AGAIN IF I MAKE CHANGES
class ninjas(models.Model):
    dojo_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # MIGRATE AND MIGRATE AGAIN IF I MAKE CHANGES

    def __repr__(self):
        return f"<User object: {self.first_name} ({self.id})>"








    def __repr__(self):
        return f"<User object: {self.first_name} ({self.id})>"
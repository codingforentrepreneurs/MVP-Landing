from django.db import models

# Create your models here.
class EmailEntry(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    # date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True) # set when saved?
    timestamp = models.DateTimeField(auto_now_add=True) # set when added?
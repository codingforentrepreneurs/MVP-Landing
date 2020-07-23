from django.db import models

# Create your models here.
class EmailEntry(models.Model):
    email = models.EmailField()
from django.contrib import admin

# Register your models here.
from .models import EmailEntry

admin.site.register(EmailEntry)
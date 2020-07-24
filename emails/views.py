from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
# Model -> View -> Template

from .models import EmailEntry


def email_entry_get_view(request, id=None, *args, **kwargs):
    # get a single item stored in the database
    # print(args, kwargs)
    # obj = EmailEntry.objects.get(id=id)
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    return HttpResponse(f"<h1>Hello {obj.email}</h1>")

# def email_entry_list_view():
#     return

# def email_entry_create_view():
#     return

# def email_entry_update_view():
#     return

# def email_entry_destroy_view():
#     return
"""
The Admin Section where i'd register all the models to be shown in the admin.
"""
from django.contrib import admin
from .models import Note
# Register your models here.

admin.site.register(Note)

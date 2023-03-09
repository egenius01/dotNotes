"""
The model Section where i'd configure all the required models.
"""
from django.db import models

class Note(models.Model):
    """
    The Notes Model: This has the configuration
    for the notes main functionality which is taking notes
    which contains the name, content, date_created, date_updated and the
    image(which only accepts urls) Fields
    """
    name = models.CharField(max_length=20)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.URLField() #Images are only accepting urls for now
    User = "Emmanuel"


    def __str__(self):
        return (str(self.name)).title()

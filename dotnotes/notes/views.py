'''
Where the views live.
'''

from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer
from rest_framework import generics



def NoteListView(request):
    '''
    This Lists all the notes you currently have.
    '''
    notes = Note.objects.all()
    print (request)
    return render(request, 'notes/index.html',context={'notes':notes})

'''

API VIEWS

'''
class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
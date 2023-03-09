"""
This is where the addresses in this app stay.
"""
from django.urls import path
from .views import NoteListView, NoteDetails, NoteList
urlpatterns = [
    path('', NoteListView, name='NoteList'),
    path('api/list', NoteList.as_view(), name='list'),
    path('api/details/<int:pk>', NoteDetails.as_view(), name='details'),

]

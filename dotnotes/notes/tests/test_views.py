from django.test import TestCase, Client
from django.urls import reverse
from ..models import Note

class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('NoteList')
        self.Note1 = Note.objects.create(
            name = 'New Note',
            content = "blablue" ,
            image = 'www.urlhere.com'
        )
    def test_note_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/index.html')
        print ('All done and shiny ')

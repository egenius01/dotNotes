from django.test import TestCase, Client
from django.urls import reverse
from ..models import Note
from rest_framework.test import APITestCase
from rest_framework import status

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


class NotesTests(APITestCase):
    def setUp(self):
        self.Note1= Note.objects.create(
            name=  'DotNote Test',
            content = 'DotNote Content',
            image = 'www.noteimage.com'
        )
    def test_create_notes(self):
        """
        Creating new notes Success
        """
        url = reverse('api-list')
        data = {
            "name": "Note 2",
            "content": "This is the content of Note 2",
            "image": "https://www.image2.com"
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Note.objects.count(), 2) #1 plus the one created above in the setup


    def test_notes_list(self):
        """
        List Notes Success
        """
         
        url = reverse('api-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Note.objects.count(), 1)
    
    def test_note_details(self):
        """
        Note Details Test
        """

        url = reverse('api-details', args=[self.Note1.id])
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_note_update(self):
        """
        Note Update Test
        """
        data = {
            'name': "New Data",
        }
        url = reverse('api-details', args=[self.Note1.id])
        response = self.client.patch(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['name'], "New Data")

    def test_note_delete(self):
        """
        Note Delete Test
        """
        url = reverse('api-details', args=[self.Note1.id])
        response = self.client.delete(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Note.objects.count(), 0)
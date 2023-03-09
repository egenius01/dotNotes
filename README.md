# DotNotes API

DotNotes is a RESTful API that allows you to create, retrieve, update, and delete notes. With DotNotes, you can easily manage your notes data in a programmatic way.

## Installation

To use DotNotes, you'll need to have Python 3 and Django 3 installed on your system. Once you have those dependencies installed, you can follow these steps to get started:

1. Clone the repository: `git clone https://github.com/your-username/dotnotes.git`
2. Install the requirements: `pip install -r requirements.txt`
3. Set up the database: `python manage.py migrate`
4. Run the server: `python manage.py runserver`

DotNotes should now be running at `http://localhost:8000/`.

## API Endpoints

DotNotes provides the following API endpoints:

### `GET /api/notes/`

Returns a list of all notes in the system.

Example response:

```json
[
{
    "id": 1,
    "name": "Note 1"
    "content": "This is the content of Note 1",
    "created_at": "2023-03-09T16:30:00Z",
    "updated_at": "2023-03-09T16:30:00Z"
    "image": "https://www.image1.com"
}
  {
    "id": 2,
    "name": "Note 2",
    "content": "This is the content of Note 2",
    "created_at": "2023-03-09T16:31:00Z",
    "updated_at": "2023-03-09T16:31:00Z"
    "image": "https://www.image2.com"

  }
]

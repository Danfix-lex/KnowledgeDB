import uuid
from django.db import models
from django.conf import settings
from user.models import Author

# Create your models here.

# class Author(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField()

class Genre(models.Model):
    GENRE_CHOICES = (
    ("R", "ROMANCE"),
    ("C", "COMEDY"),
    ("P", "POLITICS"),
    ("F", "FINANCE"),
    ("T", "TRAGEDY")
    )
    name = models.CharField(max_length=1, choices=GENRE_CHOICES, default="P")

    def __str__(self):
        return self.name

class Language(models.Model):
    LANGUAGE_CHOICES = (
    ("Y", "YORUBA"),
    ("I", "IGBO"),
    ("H", "HAUSA"),
    ("E", "ENGLISH"),
    ("F", "FRENCH"),
    ("S", "SPANISH"),
    ("R", "RUSSIAN"),
    ("P", "PORTUGUESE")
    )
    name = models.CharField(max_length=1, choices=LANGUAGE_CHOICES, default="E")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = ""
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    LOAN_STATUS = (
    ("A", "AVAILABLE"),
    ("B", "BORROWED"),
    ("M", "MAINTENANCE"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default="A", unique=True)
    return_date = models.DateTimeField(blank=True, null=False)
    comments = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
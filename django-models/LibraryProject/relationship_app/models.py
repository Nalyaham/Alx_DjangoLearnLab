from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField

class Book(models.Model):
    name = models.CharField
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField
    books = models.ManyToManyField(Book,  related_name = 'book_in_library')

class Librarian(models.Model):
    name = models.CharField
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='library')

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
            permissions = [
                 ('can_add_book', 'can add book'),
                 ('can_change_book', 'can change book'), 
                 ('can_delete_book', 'can delete book'),
            ]


class Library(models.Model):
    name = models.CharField
    books = models.ManyToManyField(Book,  related_name = 'book_in_library')

class Librarian(models.Model):
    name = models.CharField
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='library')

class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    roles = [ ('ADMIN', 'Admin'), 
             ('LIBRARIAN', 
              'Librarian'), 
              ('MEMBER' , 'Member') ]

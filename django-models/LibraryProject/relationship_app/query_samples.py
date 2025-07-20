from .models import Book, Author, Library, Librarian
author = Author.objects.get(id=1)
books = author.books.all()

library_name = 'My Library'
library = Library.objects.get(name=library_name)
book = library.book_in_library.all()

librarian = Librarian.objects.get(id=1)
library = librarian.library.all()
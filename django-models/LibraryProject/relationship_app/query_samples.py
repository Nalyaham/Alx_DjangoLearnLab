from .models import Book, Author, Library, Librarian
author = Author.objects.get(id=1)
books = author.books.all()

library = Library.objects.get(id=1)
book = library.book_in_library.all()

librarian = Librarian.objects.get(id=1)
library = librarian.library.all()
from .models import Book, Author, Library, Librarian
author_name = 'Author'
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

library_name = 'My Library'
library = Library.objects.get(name=library_name)
book = library.books.all()

librarian_name = "librarian"
librarian = Librarian.objects.get(library=library)
library = librarian.library.all()
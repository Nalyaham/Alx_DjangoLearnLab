from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Library 

# Create your views here.
def book_list(request):
    books = Book.objects.all()    
    context = {'book_list': books} 
    return render(request, 'books/book_list.html', context)

class LibraryListView(ListView):
    model = Library
    template_name = 'book_list.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.all().values('name', 'books')
    
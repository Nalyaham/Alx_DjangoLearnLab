from django.urls import path
from .views import list_books

urlpatterns = [
    path('booklist/', list_books.list_books, name='booklist'),
    path('library/', list_books.LibraryDetailView.as_view(), name='library')]

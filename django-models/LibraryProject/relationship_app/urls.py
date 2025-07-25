from django.urls import path
from django.contrib.auth import login
from .views import list_books, register, Admin, Member, Librarian, add_book, edit_book, delete_book
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    path('booklist/', list_books.list_books, name='booklist'),
    path('library/', list_books.LibraryDetailView.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'), 
	path('register/', register.as_view(template_name = 'relationship_app/signup.html'), name='register'), 
    path('Admin/', Admin.admin_view, name='admin_view'), 
    path('member/', Member.member_view, name='member_view'), 
    path('librarian/', Librarian.librarian_view, name='librarian_view'),
    path('add_book/', add_book.add_book, name='add_book_view'),
    path('edit_book/', edit_book.edit_book, name='edit_book_view'),
    path('delete_book/', delete_book.delete_book, name='delete_book_view'),
]



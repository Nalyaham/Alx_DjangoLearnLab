from django.urls import path
from .views import list_books, SignUpView, admin_view, member_view, librarian_view, add_book, edit_book, delete_book
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('booklist/', list_books.list_books, name='booklist'),
    path('library/', list_books.LibraryDetailView.as_view(), name='library'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
	path('register/', SignUpView.as_view(template_name = 'relationship_app/signup.html'), name='register'), 
    path('Admin/', admin_view.admin_view, name='admin_view'), 
    path('member/', member_view.member_view, name='member_view'), 
    path('librarian/', librarian_view.librarian_view, name='librarian_view'),
    path('AddBook/', add_book.add_book, name='add_book_view'),
    path('EditBook/', edit_book.edit_book, name='edit_book_view'),
    path('DeleteBook/', delete_book.delete_book, name='delete_book_view'),
]



from django.urls import path
from .views import views

urlpatterns = [
    path('booklist/', views.list_books, name='booklist'),
    path('library/', views.LibraryDetailView.as_view(), name='library')]

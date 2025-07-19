from django.urls import path
from .views import views

urlpatterns = [
    path('booklist/', views.book_list, name='booklist'),
    path('library/', views.LibraryListView.as_view(), name='library')]

from .views import BookList
from django.urls import path, include

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'), 
    path('api/', include('api.urls')), 
]
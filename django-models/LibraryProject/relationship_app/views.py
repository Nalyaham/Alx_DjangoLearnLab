from django.shortcuts import render, get_object_or_404
from .models import Library
from django.contrib.auth import loginview, logoutview
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required


# Create your views here.
def list_books(request):
    books = Book.objects.all()    
    context = {'book_list': books} 
    return render(request, 'relationship_app/list_books.html', context)

class LibraryListView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        return Library.objects.all().values('name', 'books')
    
class SignUpView(CreateView):
     form_class = UserCreationForm 
     success_url = reverse_lazy('login')
     template_name = 'relationship_app/signup.html'

def is_admin(user):    
    return user.UserProfile.role == 'ADMIN'

def is_librarian(user):
     return user.UserProfile.role == 'LIBRARIAN'

def is_member(user):  
    return user.UserProfile.role == 'MEMBER'

#View for the admin
@user_passes_test(is_admin)
def Admin(request):
    return render(request, 'admin_view.html')

#View for the librarian 
@user_passes_test(is_librarian)
def Librarian(request):
    return render(request, 'librarian_view.html')

#View for the member
@user_passes_test(is_member)
def Member(request):
    return render(request, 'member_view.html')

#View for adding a book to the Book model
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST': 
         name = request.POST['name']
         author = request.POST['author']
         Book.objects.create(name=name, author=author)
         return render(request, 'add_book.html')

#View for editing the book in Database 
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
         book.name = request.POST['name']    
         book.author = request.POST['author']
         book.save()
         return render(request, 'edit_book.html', {'book': book})
    
#View for deleting a book 
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return render(request, 'delete_book.html', {'book': book})




    
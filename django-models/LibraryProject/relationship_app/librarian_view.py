from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test



def is_librarian(user):
     return user.UserProfile.role == 'LIBRARIAN'

@user_passes_test(is_librarian)
def Librarian(request):
    return render(request, 'librarian_view.html')
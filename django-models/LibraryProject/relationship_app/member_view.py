from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_member(user):  
    return user.UserProfile.role == 'MEMBER'

@user_passes_test(is_member)
def Member(request):
    return render(request, 'member_view.html')
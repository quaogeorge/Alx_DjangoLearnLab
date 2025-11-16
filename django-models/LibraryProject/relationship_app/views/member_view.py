from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, 'member_view.html')
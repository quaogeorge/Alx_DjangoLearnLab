from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian, login_url='/accounts/login/')
def librarian_dashboard(request):
    return render(request, 'librarian_view.html', {})
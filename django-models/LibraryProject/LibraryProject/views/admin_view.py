from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin, login_url='/accounts/login/')
def admin_dashboard(request):
    return render(request, 'admin_view.html', {})
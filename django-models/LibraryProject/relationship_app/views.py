from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library
from django.contrib.auth.decorators import user_passes_test, login_required

def list_books(request):
    
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):

    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        # Prefetch related books and their authors to avoid N+1 queries.
        # Assumes Library has a ManyToManyField or related_name 'books' pointing to Book.
        return Library.objects.prefetch_related('books__author')
    

def is_member(user):
    return user.is_authenticated and user.groups.filter(name='Members').exists()

def is_librarian(user):
    return user.is_authenticated and user.groups.filter(name='Librarians').exists()

def is_admin(user):
    return user.is_authenticated and user.is_superuser

# Views guarded by user_passes_test
@user_passes_test(is_member, login_url='/accounts/login/')
def member_view(request):
    # Optionally include context, e.g., books for this user
    return render(request, 'relationship_app/member_view.html', {})

@user_passes_test(is_librarian, login_url='/accounts/login/')
def librarian_view(request):
    # Could include data, e.g., books to manage
    return render(request, 'relationship_app/librarian_view.html', {})

@user_passes_test(is_admin, login_url='/accounts/login/')
def admin_view(request):
    # Superuser-only view
    return render(request, 'relationship_app/admin_view.html', {})    
    
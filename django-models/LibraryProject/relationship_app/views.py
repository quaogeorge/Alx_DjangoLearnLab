from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library

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
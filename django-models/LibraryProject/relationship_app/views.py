from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    """
    Function-based view that lists all books.
    Renders relationship_app/list_books.html with context {'books': books}
    """
    # Use select_related to fetch author in the same query if Book.author is a ForeignKey
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """
    Class-based view (DetailView) that displays details for a specific Library.
    Exposes the library object in the template as 'library'.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
        # Prefetch related books and their authors to avoid N+1 queries.
        # Assumes Library has a ManyToManyField or related_name 'books' pointing to Book.
        return Library.objects.prefetch_related('books__author')
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Library


# --- Function-Based View ---
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# --- Class-Based View ---
class LibraryDetailView(View):
    def get(self, request, pk):
        library = get_object_or_404(Library, pk=pk)
        return render(request, 'relationship_app/library_detail.html', {'library': library})

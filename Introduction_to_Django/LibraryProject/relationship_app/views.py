from django.shortcuts import render
from .models import Book  # make sure this import is here

def list_books(request):
    books = Book.objects.all()  # this is the missing line
    return render(request, 'relationship_app/list_books.html', {'books': books})

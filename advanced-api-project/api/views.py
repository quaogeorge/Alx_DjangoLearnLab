from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
Generic Views for CRUD Operations on the Book model.
Each view is designed to focus on one specific action:
- ListAPIView: retrieve all books
- RetrieveAPIView: retrieve a single book
- CreateAPIView: add a new book
- UpdateAPIView: modify existing book
- DestroyAPIView: delete a book
"""


# Anyone can view the list of books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Anyone can view details of a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Only authenticated users can create a book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Custom behavior: print user and clean incoming data
    def perform_create(self, serializer):
        # Additional logic can be added here
        serializer.save()


# Only authenticated users can update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


# Only authenticated users can delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
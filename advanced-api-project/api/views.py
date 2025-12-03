from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


"""
BookListView now supports:
- Filtering (title, publication_year, author)
- Searching (title, author name)
- Ordering (title, publication_year)
These features make the API more flexible and user-friendly.
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # DRF backends for filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # FILTERING — users can filter by these fields directly in query parameters
    filterset_fields = ['title', 'publication_year', 'author']

    # SEARCHING — enables ?search=keyword
    search_fields = ['title', 'author__name']

    # ORDERING — enables ?ordering=title or ?ordering=-publication_year
    ordering_fields = ['title', 'publication_year']
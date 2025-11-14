# Import the Book model
from bookshelf.models import Book

# Delete the book you created
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by retrieving all books
Book.objects.all()

# Expected output:
# <QuerySet []>
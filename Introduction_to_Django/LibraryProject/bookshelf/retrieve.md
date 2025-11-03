# Retrieve the book you created
book = Book.objects.get(title="1984")
book

# Expected output:
# <Book: 1984 by George Orwell (1949)>
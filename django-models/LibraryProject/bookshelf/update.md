book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.all()
# Expected Output: <QuerySet [<Book: Nineteen Eighty-Four by George Orwell>]>
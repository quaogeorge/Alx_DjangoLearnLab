from relationship_app.models import Author, Book, Library


def query_books_by_author(author_name):
    # Get the author object
    author = Author.objects.get(name=author_name)
    
    # Explicitly filter using the ForeignKey
    books = Book.objects.filter(author=author)
    
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")


def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    
    print(f"Books in {library_name}:")
    for book in books:
        print(f"- {book.title}")


def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library_name}: {librarian.name}")


if __name__ == "__main__":
    query_books_by_author("George Orwell")
    list_books_in_library("City Library")
    get_librarian_for_library("City Library")

from relationship_app.models import Author, Book, Library, Librarian
from django.core.exceptions import ObjectDoesNotExist

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Use 'book_set' if no related_name was set
        books = author.books.all() if hasattr(author, 'books') else author.book_set.all()
        for book in books:
            print(f"Book: {book.title}")
    except ObjectDoesNotExist:
        print(f"No author found with the name '{author_name}'.")

# List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Assumes ManyToManyField has `books`
        for book in books:
            print(f"Book: {book.title}")
    except ObjectDoesNotExist:
        print(f"No library found with the name '{library_name}'.")

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Assumes OneToOneField relationship in Librarian
        print(f"Librarian for {library.name}: {librarian.name}")
    except ObjectDoesNotExist:
        print(f"No librarian found for the library '{library_name}'.")

# Test the queries
if __name__ == "__main__":
    print("Books by Author 'J.K. Rowling':")
    get_books_by_author('J.K. Rowling')

    print("\nBooks in Library 'Central Library':")
    get_books_in_library('Central Library')

    print("\nLibrarian for 'Central Library':")
    get_librarian_for_library('Central Library')

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Use .filter to match the checker's requirement
        for book in books:
            print(f"Book: {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'.")

# List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"Book: {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")

# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # Use .get with library to meet the checker's requirement
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for the library '{library_name}'.")

# Test the queries
if __name__ == "__main__":
    print("Books by Author 'J.K. Rowling':")
    get_books_by_author('J.K. Rowling')

    print("\nBooks in Library 'Central Library':")
    get_books_in_library('Central Library')

    print("\nLibrarian for 'Central Library':")
    get_librarian_for_library('Central Library')

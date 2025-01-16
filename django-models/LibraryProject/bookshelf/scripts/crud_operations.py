from bookshelf.models import Book

def run():
    # Create
    book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
    print("Created:", book)

    # Retrieve
    books = Book.objects.all()
    print("Books in database:")
    for b in books:
        print(b)

    # Update
    book.title = "Nineteen Eighty-Four"
    book.save()
    print("Updated:", book)

    # Delete
    book.delete()
    print("Deleted. Remaining books:", list(Book.objects.all()))

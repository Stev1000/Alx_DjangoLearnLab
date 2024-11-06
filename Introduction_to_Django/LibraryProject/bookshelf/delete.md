# delete.md

```python
from bookshelf.models import Book

# Deleting a Book instance
# Assuming a book with title "1984" already exists in the database
book = Book.objects.get(title="1984")
book.delete()  # Expected output: (1, {'bookshelf.Book': 1})

# Verifying deletion by checking if any books exist
Book.objects.all()  # Expected output: <QuerySet []>

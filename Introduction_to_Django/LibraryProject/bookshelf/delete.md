# Delete Operation

**Command:**

```python
from bookshelf.models import Book

# Assume we already have a book object
book = Book.objects.get(id=1)  # Replace with a valid ID
book.delete()

# Verify if the book was deleted
books = Book.objects.all()
print(list(books))

#output 

[]  # The book list is empty after deletion

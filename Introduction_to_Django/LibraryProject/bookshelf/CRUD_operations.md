# CRUD Operations for Book Model

## Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>

## Retrieve
from bookshelf.models import Book
Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

## Update

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

## Delete

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output: <QuerySet []>

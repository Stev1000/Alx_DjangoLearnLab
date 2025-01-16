# Retrieve Operation

**Command:**

```python
# Retrieve all books
books = Book.objects.all()
for book in books:
    print(book)

# Retrieve a specific book by ID
specific_book = Book.objects.get(id=1)
print(specific_book)

# Retrieve a specific book by title
specific_book_by_title = Book.objects.get(title="1984")
print(specific_book_by_title)

# delete.md

```python
# Deleting the book instance
book.delete()  # Expected output: (1, {'bookshelf.Book': 1})

# Verifying deletion by checking if any books exist
Book.objects.all()  # Expected output: <QuerySet []>

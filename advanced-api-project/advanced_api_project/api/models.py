from django.db import models

class Author(models.Model):
    """
Author model: Represents a writer with a one-to-many relationship with books.
Book model: Stores book information including a foreign key to the Author model.
"""
     # The Author model represents a book author with their name.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

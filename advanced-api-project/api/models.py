from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Return the author's name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Reference to Author model
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Add the price field

    def __str__(self):
        return self.title  # Return the book's title

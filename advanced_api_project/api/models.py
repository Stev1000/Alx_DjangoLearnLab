from django.db import models

# Author model to store authors' details
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name

# Book model to store books' details
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book's title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # One-to-Many relationship

    def __str__(self):
        return self.title

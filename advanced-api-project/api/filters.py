from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    """
    Custom filterset for the Book model.
    Allows filtering by title, author, and publication_year.
    """
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],  # Case-insensitive containment
            'author': ['icontains'],
            'publication_year': ['exact', 'gte', 'lte'],  # Exact, greater than or equal, less than or equal
        }

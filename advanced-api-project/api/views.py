from rest_framework import generics
from django_filters import rest_framework  # <-- Correct import
from rest_framework.filters import SearchFilter, OrderingFilter  # <-- Ensure correct import here
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend 
import django_filters

# Create a filter for the Book model
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title contains')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Author contains')
    publication_year = django_filters.NumberFilter(lookup_expr='exact', label='Publication year')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# ListView: Retrieve all books with filtering, searching, and ordering
from rest_framework.filters import SearchFilter, OrderingFilter  # Ensure correct imports
from django_filters.rest_framework import DjangoFilterBackend  # Ensure correct import

class BookListView(generics.ListAPIView):
    """
    View to list all books in the system with filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter  # Filter by title, author, and publication_year
    search_fields = ['title', 'author']  # Search by title and author
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title and publication year
    ordering = ['title']  # Default ordering


# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow everyone to view details

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        # Custom behavior: Assign logged-in user as author
        serializer.save(author=self.request.user)

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
import django_filters

# Create a filter for Book model
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title contains')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Author contains')
    publication_year = django_filters.NumberFilter(lookup_expr='exact', label='Publication year')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# ListView: Retrieve all books with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    """
    View to list all books in the system with the ability to filter by title, author, or publication year,
    search by title or author, and order by title or publication year.
    Accessible to unauthenticated users (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Enable filtering, searching, and ordering
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    
    # Allow ordering by specific fields
    ordering_fields = ['title', 'publication_year']  # Fields to allow ordering by
    ordering = ['title']  # Default ordering field (ascending order)

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

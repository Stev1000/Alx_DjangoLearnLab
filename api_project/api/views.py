from rest_framework.generics import ListAPIView  # Import for ListAPIView
from rest_framework import viewsets  # Import for ViewSet
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly



# View for listing all books (for the current task)
class BookList(ListAPIView):
    """
    A view for listing all books using generics.ListAPIView.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet for performing CRUD operations on the Book model (for a future task)
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for performing CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


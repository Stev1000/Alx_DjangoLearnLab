# api/views.py
from rest_framework.generics import ListAPIView  # Import ListAPIView
from .models import Book  # Import the Book model
from .serializers import BookSerializer  # Import the BookSerializer

# Define the BookList view
class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetches all book records from the database
    serializer_class = BookSerializer  # Uses the BookSerializer to convert data to JSON

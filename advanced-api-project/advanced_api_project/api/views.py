from rest_framework.generics import ListAPIView
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# View for listing all authors
class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# View for listing all books
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

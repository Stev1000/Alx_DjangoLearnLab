# api/views.py
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Task 1: BookList using ListAPIView
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Task 2: BookViewSet using ModelViewSet (for CRUD operations)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

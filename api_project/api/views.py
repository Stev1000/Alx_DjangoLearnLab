# api/views.py
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import viewsets 
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Task 1: List view (just for listing books)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Task 2: CRUD operations (BookViewSet with CRUD)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
     # If you want different permissions for different actions:
    def get_permissions(self):
        if self.action == 'list':  # For example, only admins can view the list
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet, AuthorViewSet

# Initialize DefaultRouter for viewsets
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')  # CRUD operations for books
router.register(r'authors', AuthorViewSet, basename='authors')  # CRUD operations for authors

urlpatterns = [
    # URL for listing all books using a generic view
    path('books/', BookList.as_view(), name='book-list'),

    # Include router-generated routes for viewsets
    path('', include(router.urls)),
]

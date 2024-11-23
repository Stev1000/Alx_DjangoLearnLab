from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize the router for CRUD operations
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Task 1: URL for BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view

    # Task 2: Include all the CRUD routes from BookViewSet
    path('', include(router.urls)),  # This includes all routes registered with the router
]

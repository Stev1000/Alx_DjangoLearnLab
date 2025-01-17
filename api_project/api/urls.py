from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize the router for CRUD operations
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# URL patterns
urlpatterns = [
    # List view (GET /books/)
    path('books/', BookList.as_view(), name='book-list'),
    
    # Include router-generated routes for CRUD operations (GET, POST, PUT, DELETE)
    path('', include(router.urls)),
]

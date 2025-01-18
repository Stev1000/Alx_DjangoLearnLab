from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize the router for CRUD operations
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # URL for the BookList view (required for the current task)
    path('books/', BookList.as_view(), name='book-list'),
    path('auth-token/', obtain_auth_token, name='api_token_auth'),
    # Include router-generated routes for CRUD operations (for the future task)
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]

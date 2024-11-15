# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # For the list of books
    path('library/<int:pk>/', views.library_detail, name='library_detail'),  # For library details
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout page
    path('register/', register_view, name='register'),  # Registration page
]
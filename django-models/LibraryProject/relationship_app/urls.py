from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    list_books, 
    LibraryDetailView, 
    register, 
    admin_view, 
    librarian_view, 
    member_view,
    add_book, 
    edit_book, 
    delete_book
)

urlpatterns = [
    # Book-related paths
    path('add_book/', add_book, name='add_book'),  # Add book explicitly
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),  # Edit book explicitly
    path('books/', list_books, name='list_books'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),

    # Library detail path
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication paths
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # User registration and role-specific views
    path('register/', register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

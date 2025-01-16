from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register
from . import views  # Import views to use views.register
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    # Existing views
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view

    # Authentication views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # Explicitly use views.register
   
    # Role-based access URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]   

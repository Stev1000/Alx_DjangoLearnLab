from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('add_book/', views.add_book, name='add_book'),  # Corrected path
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  # Corrected path
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
]

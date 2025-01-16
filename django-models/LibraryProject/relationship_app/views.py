from django.shortcuts import render
from django.views.generic.detail import DetailView  # Explicit import
from .models import Library, Book  # Ensure models are imported

# Function-based view to list books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

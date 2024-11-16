# relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  # Ensure Library is imported here

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display a specific library and list all its books
class LibraryDetailView(DetailView):
    model = Library  # We're working with the Library model
    template_name = 'relationship_app/library_detail.html'  # Template for the library details
    context_object_name = 'library'  # The object will be named 'library' in the context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add books related to this library to the context
        return context
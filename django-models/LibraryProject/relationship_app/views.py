from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Library, Book  # Import the Library model

# Function-based view for the home page
def home_view(request):
    return HttpResponse("Welcome to the Library Project!")

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # We're working with the Library model
    template_name = 'relationship_app/library_detail.html'  # Create this template to display the details
    context_object_name = 'library'  # The object in context will be named 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books related to the library to the context
        context['books'] = self.object.books.all()  # Assuming ManyToManyField between Library and Book
        return context

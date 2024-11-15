# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import your models here

# Function-based View to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Specify the template for the view
    context_object_name = 'library'  # Name to use in the template context

    def get_context_data(self, **kwargs):
        # Get the context data to pass to the template
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add the books related to the library
        return context
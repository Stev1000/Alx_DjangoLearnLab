# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import your models here

# Function-based View to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'list_books.html', {'books': books})

def library_detail(request, pk):
    library = Library.objects.get(pk=pk)
    return render(request, 'library_detail.html', {'library': library}) 

from django.shortcuts import render
from .models import Book  # Assuming 'Book' is the model that holds your books

def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'books/book_list.html', {'books': books})

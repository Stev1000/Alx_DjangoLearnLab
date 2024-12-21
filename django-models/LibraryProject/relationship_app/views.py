from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Library  # Import the Book and Library models

# Existing function-based view for the home page
def home_view(request):
    return HttpResponse("Welcome to the Library Project!")

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # We're working with the Library model
    template_name = 'relationship_app/library_detail.html'  # Template to display details
    context_object_name = 'library'  # The object in context will be named 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books related to the library to the context
        context['books'] = self.object.books.all()  # Assuming ManyToManyField between Library and Book
        return context

# Authentication views

# Login view (using Django's built-in LoginView)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'  # Custom template for login

# Logout view (using Django's built-in LogoutView)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'  # Template for logout confirmation

# Register view (using Django's built-in UserCreationForm)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.save())  # Log in the user after registration
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

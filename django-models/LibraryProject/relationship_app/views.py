from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView  # Import the DetailView class
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
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

# Authentication views

# Custom Login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Custom Logout view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('/')  # Redirect to homepage after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

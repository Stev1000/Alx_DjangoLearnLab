from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Library, Book
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

# Function-based view to list books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome, {username}! Your account has been created.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Check if the user has the 'Admin' role
def is_admin(user):
    return user.is_authenticated and user.profile.role == 'Admin'

# Check if the user has the 'Librarian' role
def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'

# Check if the user has the 'Member' role
def is_member(user):
    return user.is_authenticated and user.profile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})
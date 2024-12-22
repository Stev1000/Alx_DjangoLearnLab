from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth.decorators import user_passes_test

# Function-based view for the home page
def home_view(request):
    return HttpResponse("Welcome to the Library Project!")

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Role-based views
def admin_check(user):
    return user.userprofile.role == 'Admin'

def librarian_check(user):
    return user.userprofile.role == 'Librarian'

def member_check(user):
    return user.userprofile.role == 'Member'

# Admin view - Only Admin can access
@user_passes_test(admin_check)
def admin_view(request):
    return HttpResponse("Welcome Admin")

# Librarian view - Only Librarian can access
@user_passes_test(librarian_check)
def librarian_view(request):
    return HttpResponse("Welcome Librarian")

# Member view - Only Member can access
@user_passes_test(member_check)
def member_view(request):
    return HttpResponse("Welcome Member")

# Class-based view for Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

# Authentication views

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

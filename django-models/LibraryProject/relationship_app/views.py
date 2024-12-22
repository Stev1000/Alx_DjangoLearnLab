from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library, UserProfile, Author
from django.contrib.auth.decorators import user_passes_test, permission_required  # Corrected import

# Function-based view for the home page
def home_view(request):
    return HttpResponse("Welcome to the Library Project!")

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Role-based access checks
def is_member(user):
    return user.userprofile.role == 'Member'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin view - Only Admin can access
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view - Only Librarian can access
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view - Only Member can access
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Add book view - Only users with can_add_book permission can add books
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author_id = request.POST['author']
        publication_year = request.POST['publication_year']
        author = Author.objects.get(id=author_id)
        book = Book.objects.create(
            title=title, author=author, publication_year=publication_year
        )
        return redirect('list_books')
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

# Edit book view - Only users with can_change_book permission can edit books
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = Author.objects.get(id=request.POST['author'])
        book.publication_year = request.POST['publication_year']
        book.save()
        return redirect('list_books')
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

# Delete book view - Only users with can_delete_book permission can delete books
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

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
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

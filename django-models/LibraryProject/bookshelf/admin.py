from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display the title, author, and publication year in the list view
    list_display = ('title', 'author', 'publication_year')
    # Add filters for publication year
    list_filter = ('publication_year',)
    # Enable search functionality for title and author
    search_fields = ('title', 'author')

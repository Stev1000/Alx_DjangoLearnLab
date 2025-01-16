from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the list view
    list_filter = ('publication_year',)  # Add filter options for publication_year
    search_fields = ('title', 'author')  # Add search functionality for title and author fields

admin.site.register(Book, BookAdmin)

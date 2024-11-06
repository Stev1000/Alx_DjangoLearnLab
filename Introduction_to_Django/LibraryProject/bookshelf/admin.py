# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Customize the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality
    search_fields = ['title', 'author']
    
    # Add filtering by publication year
    list_filter = ('publication_year',)

# Register the Book model with the custom admin interface
admin.site.register(Book, BookAdmin)



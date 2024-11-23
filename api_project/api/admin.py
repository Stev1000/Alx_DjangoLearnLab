from django.contrib import admin
from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Adjust fields as per your model

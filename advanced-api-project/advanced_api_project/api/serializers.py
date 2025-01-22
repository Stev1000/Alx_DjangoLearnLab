from rest_framework import serializers
from .models import Author, Book

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Validate that the publication year is not in the future
    def validate_publication_year(self, value):
        from datetime import date
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include author's name and related books

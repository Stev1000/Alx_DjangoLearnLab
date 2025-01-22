from django.test import TestCase
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer
from rest_framework.test import APIClient
from rest_framework import status

class AuthorModelTest(TestCase):
    def test_author_creation(self):
        author = Author.objects.create(name="J.K. Rowling")
        self.assertEqual(author.name, "J.K. Rowling")

class BookModelTest(TestCase):
    def test_book_creation(self):
        author = Author.objects.create(name="J.K. Rowling")
        book = Book.objects.create(title="Harry Potter", publication_year=1997, author=author)
        self.assertEqual(book.title, "Harry Potter")
        self.assertEqual(book.publication_year, 1997)
        self.assertEqual(book.author.name, "J.K. Rowling")

class BookSerializerTest(TestCase):
    def test_valid_book_serializer(self):
        author = Author.objects.create(name="J.K. Rowling")
        book_data = {
            "title": "Harry Potter",
            "publication_year": 1997,
            "author": author.id,
        }
        serializer = BookSerializer(data=book_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_publication_year(self):
        author = Author.objects.create(name="J.K. Rowling")
        book_data = {
            "title": "Harry Potter",
            "publication_year": 3000,  # Future year
            "author": author.id,
        }
        serializer = BookSerializer(data=book_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("publication_year", serializer.errors)

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)

    def test_get_authors(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "J.K. Rowling")

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        # Create sample authors
        self.author_a = Author.objects.create(name="Author A")
        self.author_b = Author.objects.create(name="Author B")

        # Create sample books using the author instances
        self.book1 = Book.objects.create(title="Sample Book 1", author=self.author_a, price=19.99)
        self.book2 = Book.objects.create(title="Sample Book 2", author=self.author_b, price=25.00)

        # Define API endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.id})

    def test_create_book(self):
        # Use an existing author or create a new one
        data = {
            "title": "New Book",
            "author": self.author_a.id,  # Use the ID of an existing author
            "price": 29.99
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Sample Book 1")

    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "author": self.author_b.id,  # Use the ID of an existing author
            "price": 25.00
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        # Filter by Author A
        response = self.client.get(self.list_url, {'author': self.author_a.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author_a.id)

        # Filter by non-existent author
        response = self.client.get(self.list_url, {'author': 999})  # Non-existent ID
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

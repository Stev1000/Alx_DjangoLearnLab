# blog/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login(self):
        # Test login page
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Test successful login
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertRedirects(response, reverse('home'))  # Redirects to home page after login

    def test_register(self):
        # Test registration page
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        # Test registration form submission
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'password123', 'password2': 'password123'})
        self.assertRedirects(response, reverse('login'))  # Redirect to login after registration

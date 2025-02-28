from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, date_of_birth, password, **extra_fields)


# Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensures email is unique
    date_of_birth = models.DateField(null=True, blank=True)  # New custom field
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # New custom field

    objects = CustomUserManager()  # Links to the custom user manager

    USERNAME_FIELD = 'email'  # Email used for authentication
    REQUIRED_FIELDS = ['date_of_birth']  # Additional required fields

    def __str__(self):
        return self.email


# UserProfile Model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Links to CustomUser
    bio = models.TextField(blank=True, null=True)  # Optional biography
    location = models.CharField(max_length=100, blank=True, null=True)  # Optional location
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Optional profile picture

    def __str__(self):
        return f"{self.user.email}'s Profile"


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

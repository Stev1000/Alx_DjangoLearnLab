# Advanced API Project

This project demonstrates the implementation of a CRUD API for managing books using Django REST Framework (DRF). It includes customizations, permissions, and proper documentation.

## Features

1. **List All Books**
   - URL: `/books/`
   - Method: `GET`
   - Description: Retrieves a list of all books. Accessible to everyone.

2. **Retrieve a Specific Book**
   - URL: `/books/<int:pk>/`
   - Method: `GET`
   - Description: Retrieves details of a specific book by ID. Accessible to everyone.

3. **Create a Book**
   - URL: `/books/create/`
   - Method: `POST`
   - Description: Allows authenticated users to create a new book.

4. **Update a Book**
   - URL: `/books/<int:pk>/update/`
   - Method: `PUT`
   - Description: Allows authenticated users to update an existing book.

5. **Delete a Book**
   - URL: `/books/<int:pk>/delete/`
   - Method: `DELETE`
   - Description: Allows authenticated users to delete a book.

## Permissions

- `IsAuthenticatedOrReadOnly`: Applied to `ListView` and `DetailView` to allow read-only access for unauthenticated users.
- `IsAuthenticated`: Applied to `CreateView`, `UpdateView`, and `DeleteView` to restrict write access to authenticated users only.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd advanced_api_project

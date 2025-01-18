from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, UserProfile


# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('email', 'password', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active')}
        ),
    )
    list_display = ('email', 'date_of_birth', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)


# Book Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the admin list view
    list_filter = ('publication_year',)  # Add filter options for publication_year
    search_fields = ('title', 'author')  # Add search functionality for title and author fields

admin.site.register(Book, BookAdmin)


# UserProfile Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')  # Display user and location in admin
    search_fields = ('user__email', 'location')  # Enable search by email and location

admin.site.register(UserProfile, UserProfileAdmin)

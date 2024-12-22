from django.contrib import admin
from django.urls import path, include
from relationship_app.views import home_view, admin_view, librarian_view, member_view, LibraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('relationship/', include('relationship_app.urls')),  # Include URLs from the relationship app
    
    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

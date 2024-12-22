from django.contrib import admin
from django.urls import path, include
from relationship_app.views import home_view  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Root URL that routes to the home view
    path('relationship/', include('relationship_app.urls')),  # Include URLs from the relationship app
]

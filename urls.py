from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel URL
    path'', include('tracker.urls')),  # Include URLs from the tracker app
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel URL
    path('tracker/', include('tracker.urls')),  # Include URLs from the tracker app
    path('expenses/', include('expenses.urls')), # Include URLs from the expenses app
    path('accounts/', include('accounts.urls')) # Include URLs from the accounts app
]

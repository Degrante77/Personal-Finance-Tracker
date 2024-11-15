from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Add other custom URLs here, if needed
]

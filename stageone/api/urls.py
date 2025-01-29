from django.urls import path
from .views import service

urlpatterns = [
    # Example path
    path('service', service),
    # Add more paths as needed
]
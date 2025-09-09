# alx_travel_app/listings/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'destinations', DestinationViewSet, basename='destination')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
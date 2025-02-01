from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import BookingView, ListingView

router = DefaultRouter()
router.register(r'bookings', BookingView, basename='booking')
router.register(r'listings', ListingView, basename='listing')

urlpatterns = [
    path('', include(router.urls)),
]
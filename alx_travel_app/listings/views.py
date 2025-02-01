from django.shortcuts import render
from .models import Booking, Listing
from .serializers import BookingSerializer, ListingSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .tasks import send_booking_confirmation_email

# Create your views here.
class BookingView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        booking = serializer.save()
        user_email = booking.user.email
        booking_details = f'Listing: {booking.host_listing.title}\nStatus: {booking.status}'

        send_booking_confirmation_email.delay(user_email, booking_details)

class ListingView(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
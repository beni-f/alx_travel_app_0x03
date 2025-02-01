# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Status(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    CONFIRMED = 'Confirmed', 'Confirmed'
    CANCELLED = 'Cancelled', 'Cancelled'

class Listing(models.Model):
    title = models.CharField(max_length=64, null=False)
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=128)
    price = models.IntegerField()
    amenities = models.TextField()
    availability = models.BooleanField(null=False, default=True)
    host_user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
class Booking(models.Model):
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    host_listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE
    )

class Review(models.Model):
    rating = models.IntegerField(null=True)
    review = models.TextField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE
    )

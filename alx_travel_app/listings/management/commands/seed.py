from django.contrib.auth import get_user_model
from models import Status, Listing, Booking, Review

User = get_user_model()

host_user = User.objects.create_user(username='hostuser', password='password123', email='host@example.com')
regular_user = User.objects.create_user(username='regularuser', password='password123', email='regular@example.com')

listing1 = Listing.objects.create(
    title="Cozy Apartment",
    description="A cozy apartment in the city center",
    location="123 Main Street, Cityville",
    price=120,
    amenities="WiFi, TV, Kitchen",
    availability=True,
    host_user=host_user
)

listing2 = Listing.objects.create(
    title="Beachside Villa",
    description="A luxurious villa near the beach",
    location="456 Ocean Drive, Beachtown",
    price=300,
    amenities="Pool, WiFi, Breakfast",
    availability=True,
    host_user=host_user
)

# Create test bookings
booking1 = Booking.objects.create(
    status=Status.PENDING,
    user=regular_user,
    host_listing=listing1
)

booking2 = Booking.objects.create(
    status=Status.CONFIRMED,
    user=regular_user,
    host_listing=listing2
)

# Create test reviews
review1 = Review.objects.create(
    rating=5,
    review="Amazing stay, very clean and comfortable!",
    user=regular_user,
    booking=booking2
)

review2 = Review.objects.create(
    rating=3,
    review="Decent place but could use some improvements.",
    user=regular_user,
    booking=booking1
)

print("Seeding completed successfully!")

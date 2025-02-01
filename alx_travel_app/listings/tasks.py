from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(user_email, booking_details):
    subject = 'Booking Confirmation'
    message = f'Dear User,\n\nYour booking has been confirmed. Details:\n\n{booking_details}'

    send_mail(
        subject,
        message,
        "noreply@myapp.com",
        [user_email],
        fail_silently=False,
    )

    return "Email sent successfully"
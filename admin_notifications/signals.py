from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from oscar.core.loading import get_model

Order = get_model('order', 'Order')

@receiver(post_save, sender=User)
def new_user_notification(sender, instance,update_fields, created, **kwargs):
    if created:
        subject = 'New User Registration'
        message = f'A new user registered: {instance.username}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]  # Replace with the admin's email

        send_mail(subject, message, from_email, recipient_list)

@receiver(post_save, sender=Order)
def order_place(sender, instance, update_fields, created, **kwargs):
    if instance.status == 'Paid':
        subject = 'New order'
        message = f'User place a new order basket id: {instance.basket_id}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]  # Replace with the admin's email

        send_mail(subject, message, from_email, recipient_list)
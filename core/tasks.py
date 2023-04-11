# from django.core.mail import EmailMultiAlternatives
# from django.conf import settings
# from .models import Subscriber 
# from baseuser.models import BaseUser
# from django.db.models import Q
# from celery import shared_task

# @shared_task
# def send_mail_to_subscibers():
#     subscribers = Subscriber.objects.filter(is_active=True)
#     subscriber_emails = subscribers.values_list('email', flat=True)
#     user_emails = BaseUser.objects.filter(Q(is_active=True) & Q(email__isnull=False)).values_list('email', flat=True)
#     email_list = list(set(list(subscriber_emails) + list(user_emails)))
#     if not email_list:
#         return

#     mail_text = "Hello"

#     # Create the email message and send it
#     msg = EmailMultiAlternatives(subject="Hello", body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list)
#     msg.attach_alternative(mail_text, "text/html")
#     msg.send()

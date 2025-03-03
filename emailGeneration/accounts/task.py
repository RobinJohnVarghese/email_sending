from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Email

@shared_task
def send_all_emails():
    email_records = Email.objects.all()
    for email_record in email_records:
        send_mail(
            email_record.subject,
            email_record.message,
            settings.DEFAULT_FROM_EMAIL,
            [email_record.recipient],
            fail_silently=False,
        )
    return "All emails sent."

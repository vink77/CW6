import os
import django

from client.models import Logs, Message

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import datetime
from smtplib import SMTPException
from django.core.mail import send_mail
from decouple import config
import pytz


def send_messages():
    now = datetime.datetime.now()
    for messaging in Message.objects.filter(mailing_status=Message.STATUS_STARTED):
        for message_client in messaging.mailing_clients.all():
            mailing_log = Logs.objects.filter(log_client=message_client, log_mailing=mailing)
            if mailing_log.exists():
                last_try = mailing_log.order_by('-created_time').first()
                desired_timezone = pytz.timezone('Europe/Moscow')
                last_try_date = last_try.created_time.astimezone(desired_timezone)
                if messaging.PERIOD_DAILY:
                    if (now.date() - last_try_date.date()).days >= 1:
                        send_email(messaging, message_client)
                elif messaging.PERIOD_WEEKLY:
                    if (now.date() - last_try_date.date()).days >= 7:
                        send_email(messaging, message_client)
                elif messaging.PERIOD_MONTHLY:
                    if (now.date() - last_try_date.date()).days >= 30:
                        send_email(messaging, message_client)
            else:
                send_email(messaging, message_client)


def send_email(messaging, message_client):
    subject = messaging.subject
    message = messaging.body
    from_email = config('EMAIL_HOST_USER')
    recipient_list = [message_client.email]
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        Logs.objects.create(
            log_status=Logs.STATUS_OK,
            log_client=message_client,
            log_mailing=messaging,
            response='отправлено'
        )

    except SMTPException as e:
        Logs.objects.create(
            log_status=Logs.STATUS_FAILED,
            log_client=message_client,
            log_mailing=messaging,
            response=e
        )


if __name__ == '__main__':
    send_messages()
import os

import django
from apscheduler.schedulers.blocking import BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job

from django.conf import settings

from client.models import Logs, Message

import datetime
from smtplib import SMTPException
from django.core.mail import send_mail
import pytz


def send_messages():
    # Creates a default Background Scheduler
    sched = BlockingScheduler()

    now = datetime.datetime.now()
    for messaging in Message.objects.filter(status=Message.STATUS_STARTED):
        data_create = messaging.data_create
        if messaging.PERIOD_DAILY:
            sched.add_job(send_email(messaging), 'interval', day=1 )

        elif messaging.PERIOD_WEEKLY:
            sched.add_job(send_email(messaging), 'interval', day=7 )

        elif messaging.PERIOD_MONTHLY:
            sched.add_job(send_email(messaging), 'interval', day=30 )
        else:
            send_email(messaging)


    sched.start()

def send_email(messaging):
    now = datetime.datetime.now()

    message = messaging.message_body
    from_email = settings.EMAIL_HOST_USER
    try:
        send_mail(
            message=message,
            from_email=from_email,
            recipient_list=messaging.client.email,
            fail_silently=False,
        )
        Logs.objects.create(
            status=Logs.STATUS_OK,
            message=message,
            client=messaging.client.email,
            last_try=now,
            response='отправлено'
        )

    except SMTPException as e:
        Logs.objects.create(
            status=Logs.STATUS_FAILED,
            message=message,
            client=messaging.client.email,
            last_try=now,
            response=e
        )


if __name__ == '__main__':
    send_messages()
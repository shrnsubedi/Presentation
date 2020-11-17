from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.shortcuts import render

@shared_task
def add(x,y):
    sleep(4)
    return x+y

@shared_task
def mul(x,y):
    sleep(4)
    return x*y

@shared_task(bind=True)
def go_to_sleep(self,time):
    sleep(time)
    return 'Done'

@shared_task
def eml(fromML,toML):
    sleep(4)
    mail=send_mail('Celery Task Worked',
    'This is proof that task worked',
    fromML,
    [toML]
    )
    return 'Mail Sent successfully' if mail==1 else 'Mail Failed!'





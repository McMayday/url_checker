from __future__ import absolute_import, unicode_literals
from celery import Celery
from .models import *
import requests
from celery import shared_task
from urlchecker.celery import app as celery_app
from django_celery_beat.models import PeriodicTask, IntervalSchedule




def change_status(url):
    url.url_status = requests.get(url.url_name).status_code
    url.save()


@celery_app.task
def test(time):
    schedule, created = IntervalSchedule.objects.get_or_create( every=time,  period=IntervalSchedule.SECONDS, )
    try:
        task = PeriodicTask.objects.get(name__iexact = 'check_interval')
        task.delete()
    except:
        pass
    PeriodicTask.objects.create(
    interval=schedule,
    name='check_interval',
    task='url_check.tasks.set_interval',
    )


@shared_task
def set_interval():
    urls = Url.objects.all()
    for url in urls:
        if url.url_checker == True:
            change_status(url)

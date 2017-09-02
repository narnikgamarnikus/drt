from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import Latency
import random
from channels import Group

from django.db.models import Q
import json

@periodic_task(run_every=(crontab(minute='*/1')), name="add_data", ignore_result=True)
def add_data():
	latencies = Latency.objects.all()
	for latency in latencies:
		latency.latency = random.randint(1, 999)
		latency.save()
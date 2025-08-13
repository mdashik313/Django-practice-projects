import json
from django.utils import timezone
from django.shortcuts import render, HttpResponse

from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .tasks import my_task

# Create your views here.

def schedule_task(request):

    result = my_task()

    completed_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

    return HttpResponse(f"Task Scheduled. Completed at {completed_time}. Result: {result}")

def dynamic_schedule(request):
    interval, _ = IntervalSchedule.objects.get_or_create(
        every = 30,
        period = IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval = interval,
        name = "my-dynamic-schedule",
        task = "my_app.tasks.my_task",
    )

    return HttpResponse("Task Scheduled!")
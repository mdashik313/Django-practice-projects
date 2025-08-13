from django.urls import path
from .views import schedule_task, dynamic_schedule

urlpatterns = [
    path('schedule', schedule_task, name='schedule_task'),
    path('dynamic-schedule', dynamic_schedule, name='dynamic_schedule')
]
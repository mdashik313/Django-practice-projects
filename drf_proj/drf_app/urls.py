from django.urls import path

from .views import TestView

urlpatterns = [
    path('student/', TestView.as_view(), name='get_students'),
]
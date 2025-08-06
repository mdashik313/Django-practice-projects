from django.urls import path
from .views import counter 

urlpatterns = [
    path('counter-v2', counter, name='counter-v2')
]
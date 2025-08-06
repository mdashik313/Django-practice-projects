from celery import shared_task

from .models import Counter

@shared_task
def my_counter():
    
    c, _ = Counter.objects.get_or_create(id=1)
    
    c.count += 1

    c.save()
    print("hello world from celery")
    print('count value form celery ', c.count)

    return c.count
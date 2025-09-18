import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJANGO_POSTGRESQL_DOCKERIZED.settings')
django.setup()

from counter.models import *

objects = TestModel.objects.filter(user_id__in = [1,2])

objects = {
    object.user_id : object
    for object in objects
}
print("dict = ", objects)

id1 = "1"
id2 = "2"

ob_1 = objects.get(id1)
ob_2 = objects.get(id2)
print("data = ", ob_1.name, " ", ob_2.name)

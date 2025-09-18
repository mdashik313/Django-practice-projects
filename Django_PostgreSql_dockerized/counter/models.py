from django.db import models

# Create your models here.
class Counter(models.Model):
    count = models.IntegerField(default=0)

class TestModel(models.Model):
    id1 = models.IntegerField()
    id2 = models.IntegerField()
    name = models.CharField()

    user_id = models.CharField()

    def __str__(self):
        return self.name
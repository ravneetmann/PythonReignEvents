from django.db import models


class Event(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    event_type = models.IntegerField()


    def __str__(self):
        return self.description

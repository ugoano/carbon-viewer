from django.db import models

from carbon_credentials.meters.models import Meter


class Reading(models.Model):
    consumption = models.FloatField()
    reading_date_time = models.DateTimeField()
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name='readings')

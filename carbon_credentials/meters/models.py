from django.db import models

from carbon_credentials.buildings.models import Building


class Meter(models.Model):
    id = models.IntegerField(primary_key=True)
    fuel = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='meters')

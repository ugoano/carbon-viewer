
from .models import Building
from ..meters.serializers import MeterSerializer
from rest_framework import serializers


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    meters = MeterSerializer(many=True, read_only=True)
    class Meta:
        model = Building
        fields = ['id', 'name', 'meters']

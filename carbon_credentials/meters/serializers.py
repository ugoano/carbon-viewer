
from .models import Meter
from rest_framework import serializers


class MeterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meter
        fields = ['id', 'building_id', 'fuel', 'unit', 'building']

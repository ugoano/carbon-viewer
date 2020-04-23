
from .models import Reading
from rest_framework import serializers


class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    meter = serializers.SlugRelatedField(slug_field='unit', read_only=True)

    class Meta:
        model = Reading
        fields = ['consumption', 'meter_id', 'reading_date_time', 'meter']

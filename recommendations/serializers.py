from rest_framework import serializers
from dashboard.models import SensorReading

class SensorReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = ['timestamp', 'nitrogen', 'phosphorus', 'potassium', 'ph']

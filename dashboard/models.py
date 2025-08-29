from django.db import models

# Create your models here.

from django.db import models
import random

class SensorReading(models.Model):
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    ph = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_dummy_data():
        """Simulates IoT sensor values"""
        return SensorReading.objects.create(
            nitrogen=random.uniform(10, 50),
            phosphorus=random.uniform(5, 30),
            potassium=random.uniform(20, 60),
            ph=random.uniform(5.5, 8.0)
        )


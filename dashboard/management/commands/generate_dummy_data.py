from django.core.management.base import BaseCommand
from dashboard.models import SensorReading
import random

class Command(BaseCommand):
    help = 'Generate 50 dummy SensorReading entries'

    def handle(self, *args, **kwargs):
        for _ in range(50):
            SensorReading.objects.create(
                nitrogen=random.uniform(10, 50),
                phosphorus=random.uniform(5, 30),
                potassium=random.uniform(20, 60),
                ph=random.uniform(5.5, 8.0)
            )
        self.stdout.write(self.style.SUCCESS('Successfully created 50 dummy SensorReading entries'))

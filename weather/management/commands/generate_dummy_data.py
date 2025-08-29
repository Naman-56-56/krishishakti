from django.core.management.base import BaseCommand
from weather.models import WeatherInfo
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Generate 5 dummy WeatherInfo entries'

    def handle(self, *args, **kwargs):
        now = datetime.now()
        for i in range(5):
            WeatherInfo.objects.create(
                temperature=random.uniform(20, 40),
                humidity=random.uniform(40, 90),
                rainfall_probability=random.uniform(0, 100),
                timestamp=now - timedelta(hours=i)
            )
        self.stdout.write(self.style.SUCCESS('Successfully created 5 dummy WeatherInfo entries'))

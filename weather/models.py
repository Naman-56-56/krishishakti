
# Create your models here.

from django.db import models

class WeatherInfo(models.Model):
	temperature = models.FloatField()
	humidity = models.FloatField()
	rainfall_probability = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Weather at {self.timestamp}: {self.temperature}°C, {self.humidity}% humidity, {self.rainfall_probability}% rain"

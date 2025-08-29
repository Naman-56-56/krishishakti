
# Create your models here.

from django.db import models

class FarmerProfile(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	preferred_language = models.CharField(max_length=20, choices=[('en', 'English'), ('hi', 'Hindi')], default='en')
	crops_grown = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.name} ({self.location})"

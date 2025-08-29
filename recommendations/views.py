from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from dashboard.models import SensorReading
from weather.models import WeatherInfo
from .serializers import SensorReadingSerializer

class RecommendationAPIView(APIView):
	def get(self, request):
		latest_reading = SensorReading.objects.order_by('-timestamp').first()
		latest_weather = WeatherInfo.objects.order_by('-timestamp').first()
		if not latest_reading:
			return Response({'error': 'No sensor readings found.'}, status=404)
		data = SensorReadingSerializer(latest_reading).data
		# Recommendation logic
		recommendation = ""
		if latest_weather and latest_weather.rainfall_probability > 50:
			recommendation = "Rain expected, hold fertilizer application"
		else:
			if latest_reading.nitrogen < 20:
				recommendation = "Add Urea (Nitrogen-rich fertilizer)"
			elif latest_reading.phosphorus < 10:
				recommendation = "Add DAP (Phosphorus-rich fertilizer)"
			elif latest_reading.potassium < 25:
				recommendation = "Add MOP (Potassium-rich fertilizer)"
			elif latest_reading.ph < 6.5:
				recommendation = "Adjust pH: Add lime"
			else:
				recommendation = "Soil is healthy"
		data['recommendation'] = recommendation
		return Response(data)

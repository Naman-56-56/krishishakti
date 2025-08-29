
# Create your views here.

from django.http import JsonResponse
from .models import WeatherInfo

def latest_weather(request):
	latest = WeatherInfo.objects.order_by('-timestamp').first()
	if not latest:
		return JsonResponse({'error': 'No weather info found.'}, status=404)
	data = {
		'temperature': latest.temperature,
		'humidity': latest.humidity,
		'rainfall_probability': latest.rainfall_probability,
		'timestamp': latest.timestamp,
	}
	return JsonResponse(data)

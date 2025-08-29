from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import SensorReading


# Fertilizer recommendation logic
def recommend_fertilizer(n, p, k, ph):
    if n < 20:
        return "Add Urea (Nitrogen-rich fertilizer)"
    elif p < 10:
        return "Add DAP (Phosphorus-rich fertilizer)"
    elif k < 30:
        return "Add MOP (Potassium-rich fertilizer)"
    elif ph < 6:
        return "Soil is acidic, add Lime to balance pH"
    elif ph > 7.5:
        return "Soil is alkaline, consider Gypsum"
    else:
        return "Soil nutrients look balanced 👍"

from django.http import JsonResponse

def generate_sensor_reading(request):
    if request.method == 'POST':
        reading = SensorReading.generate_dummy_data()
        return JsonResponse({
            'timestamp': str(reading.timestamp),
            'nitrogen': reading.nitrogen,
            'phosphorus': reading.phosphorus,
            'potassium': reading.potassium,
            'ph': reading.ph
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

def home(request):
    # fetch latest 10 readings
    readings = SensorReading.objects.order_by("-timestamp")[:10]

    # analyze the most recent reading for recommendation
    latest = readings[0] if readings else None
    recommendation = None
    if latest:
        recommendation = recommend_fertilizer(
            latest.nitrogen, latest.phosphorus, latest.potassium, latest.ph
        )

    # Get latest farmer profile
    from farmers.models import FarmerProfile
    farmer = FarmerProfile.objects.order_by('-id').first()
    farmer_name = farmer.name if farmer else None
    farmer_location = farmer.location if farmer else None

    return render(request, "dashboard/home.html", {
        "readings": readings,
        "recommendation": recommendation,
        "farmer_name": farmer_name,
        "farmer_location": farmer_location
    })

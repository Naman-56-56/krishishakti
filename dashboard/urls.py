from django.urls import path
from .views import home, generate_sensor_reading

urlpatterns = [
    path('', home, name='home'),
    path('generate-reading/', generate_sensor_reading, name='generate-reading'),
]

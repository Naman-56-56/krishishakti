from django.urls import path
from .views import latest_weather

urlpatterns = [
    path('api/weather/', latest_weather, name='latest-weather'),
]

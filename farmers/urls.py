from django.urls import path
from .views import register_farmer

urlpatterns = [
    path('register/', register_farmer, name='register-farmer'),
]

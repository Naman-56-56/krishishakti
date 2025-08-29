from django.urls import path
from .views import RecommendationAPIView

urlpatterns = [
    path('api/recommendation/', RecommendationAPIView.as_view(), name='recommendation-api'),
]

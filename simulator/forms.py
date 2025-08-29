from django import forms
from dashboard.models import SensorReading
from django.utils import timezone

class IoTSimulatorForm(forms.Form):
    sensor_id = forms.CharField(max_length=50, required=True)
    nitrogen = forms.IntegerField(min_value=0, required=True)
    phosphorus = forms.IntegerField(min_value=0, required=True)
    potassium = forms.IntegerField(min_value=0, required=True)
    location = forms.CharField(max_length=100, required=True)
    timestamp = forms.DateTimeField(required=False)

    def save(self):
        data = self.cleaned_data
        SensorReading.objects.create(
            nitrogen=data['nitrogen'],
            phosphorus=data['phosphorus'],
            potassium=data['potassium'],
            ph=7.0,  # Default pH, or you can add a field for it
            timestamp=data['timestamp'] if data['timestamp'] else timezone.now()
        )

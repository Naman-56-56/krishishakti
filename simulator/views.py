from django.shortcuts import render, redirect
from .forms import IoTSimulatorForm

def simulate(request):
	success = False
	if request.method == 'POST':
		form = IoTSimulatorForm(request.POST)
		if form.is_valid():
			form.save()
			success = True
			form = IoTSimulatorForm()  # Reset form after success
	else:
		form = IoTSimulatorForm()
	return render(request, 'simulator/simulate.html', {'form': form, 'success': success})
# Create your views here.

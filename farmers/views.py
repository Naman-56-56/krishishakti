
# Create your views here.

from django.shortcuts import render, redirect
from .models import FarmerProfile

def register_farmer(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		location = request.POST.get('location')
		preferred_language = request.POST.get('preferred_language')
		crops_grown = request.POST.get('crops_grown')
		FarmerProfile.objects.create(
			name=name,
			location=location,
			preferred_language=preferred_language,
			crops_grown=crops_grown
		)
		return redirect('home')
	return render(request, 'farmers/register.html')

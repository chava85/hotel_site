from django.shortcuts import render

# Create your views here.



# from .models import Customer, Rental

# Create your views here.

def index(request):
	return render(request, 'index.html')

def bookings(request):
	return render(request, 'bookings.html')
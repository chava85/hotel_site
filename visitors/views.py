from django.shortcuts import render
from .models import User
from .forms import UserForm


def index(request):
	return render(request, 'index.html')

def bookings(request):
	if request.method == 'POST':
		post = request.POST
		first_name = post['first_name']
		last_name = post['last_name']
		phone_number = post['phone_number']
	   
		user = User(first_name=first_name, last_name=last_name, 
			phone_number=phone_number)

		user.save()

	return render(request, 'bookings.html')

def show_vacancies():
	pass

def login(request):
	
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			
			return redirect('bookings.html')
						

	return render(request, 'login.html')

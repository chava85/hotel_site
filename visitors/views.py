from django.shortcuts import render

# Create your views here.



# from .models import Customer, Rental

# Create your views here.

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
        print(person)



	return render(request, 'bookings.html')


def login(request):
	return render(request, 'login.html')
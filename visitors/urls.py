from django.urls import path

from . import views

app_name = 'visitors'
urlpatterns = [
	path('', views.index, name='index'),
	path('bookings/', views.bookings, name='bookings'),
	path('login/', views.login, name='login')
]
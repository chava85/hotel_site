from django.db import models

# Create your models here.

class Customer(models.Model):
    '''To do: implement this model'''
    first_name = models.CharField(max_length=200)
    last_name = models.IntegerField(default=0)
    phone_number = models.IntegerField()


class Room(models.Model):

	room_number = models.CharField(max_length=200)
	price = models.IntegerField()

class Booking(models.Model):

	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
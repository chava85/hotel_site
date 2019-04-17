from django import forms
from django.forms import ModelForm

from .models import User

class UserForm(ModelForm):
   
	model = User
	fields = ['first_name', 'last_name', 'phone_number']
  

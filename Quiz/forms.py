from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
	
	first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	school = forms.CharField(max_length=30, required=True, help_text='Required.')
	Phone_num = forms.IntegerField(required=True, help_text='Required.')



	class Meta:
		model = User
		fields = [  'username',
					'first_name',
					'last_name',
					'Phone_num',
					'school',
					
	                    
	            ]



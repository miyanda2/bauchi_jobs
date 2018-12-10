from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *





class RegisterForm(UserCreationForm):
	
	cv = forms.FileField(required=False, label='Select a file', help_text='max. 42 megabytes')

	class Meta:
		model = User
		fields = [  'username',
					
					
	                    
	            ]



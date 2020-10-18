from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from store.models import Customer

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	
	class Meta:
		model =Customer
		fields=['username', 'email', 'phone_number','first_name', 'last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model =Customer
		fields=['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
from .models import PaymentDetail
from django import forms

class PaymentForm(forms.ModelForm):
	class Meta:
		model = PaymentDetail
		fields = ['name','contact_no','email','address','city','state','pincode']
		widgets={
			'name':forms.TextInput(attrs={ 'class':'input', 
			'placeholder':'Enter your full name here..'}
			),
			'contact_no':forms.TextInput(attrs={ 'class':'input', 
			'placeholder':'Your valid 10-digit number'}
			),
			'email':forms.TextInput(attrs={ 'class':'input', 
			'placeholder':'Your Valid Email address'}
			),
			'city':forms.TextInput(attrs={ 'class':'input', 
			'placeholder':'Enter the city name'}
			),
			'state':forms.TextInput(attrs={ 'class':'input', 
			'placeholder':'Type in your state'}
			),
			'pincode':forms.TextInput(attrs={ 'class':'input', 
			'placeholder':'Type in your area PinCode'}
			),
			'address': forms.Textarea(attrs={'class':'input', 
			'placeholder':'Enter your address.',
			'rows':2}
			),
		}
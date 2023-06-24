from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Casablanca', 'Casablanca'),
		('Rabat', 'Rabat'),
		('Tanger', 'Tanger '),
		('oujda', 'oujda'),
		('Marrakesh','Marrakesh'),
	)

	DISCRICT_CHOICES = (
		('Hay Hassani', 'Hay Hassani'), 
		('Ain Chock', 'Ain Chock'),
		('Maarif', 'Maarif'),
		('Derb koraa','Derb Koraa'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Cash', 'Cash'),
		('Credit Card','Credit Card'),
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']

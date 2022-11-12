import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):

	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer',]

class CustomerFilter(django_filters.FilterSet):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['email', 'date_created', 'payment_status', 'invoice_number', 'note', 'phone', 'image']

#Stopped in Filter Form Table Part 12 of Dennis Ivy
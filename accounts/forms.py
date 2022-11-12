from django import forms
from accounts.models import Employee, Customer, ProductForCustomer
from django.forms import ModelForm
from django.db import models
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'contact', 'email'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
                    'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
                    'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
                    }

class OrderForm(ModelForm):
        class Meta:
            model = Order
            fields = '__all__'

class CreateUserForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
        class Meta:
            model = Customer
            fields = '__all__'


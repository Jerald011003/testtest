from django import forms
from accounts.models import Employee, Customer, ProductForCustomer
from django.forms import ModelForm
from django.db import models
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

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

# class CreateUserForm(UserCreationForm):
#         class Meta:
#             model = User
#             fields = ['username', 'email', 'password1', 'password2']

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(labal='confirm Password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        foo = User.objects.filter(username=username)
        if foo.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        foo = User.objects.filter(email=email)
        if foo.exists():
            raise forms.ValidationError("Email is already taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError("Passwords are not match")
        return data


class CustomerForm(ModelForm):
        class Meta:
            model = Customer
            fields = '__all__'


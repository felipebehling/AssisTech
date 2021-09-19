from django.forms import ModelForm, fields
from django import forms
from django.forms.widgets import PasswordInput
from .models import Account
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ['username', 'email', 'cpf', 'password1', 'password2'] #Campos que vão para o Register. (são do model Account em models.) 


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Passsword', widget=PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		if not authenticate(email=email, password=password):
			raise forms.ValidationError('Login Inválido!')
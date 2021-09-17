from django.forms import ModelForm
from .models import Account
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ['username', 'email', 'cpf' , 'password1', 'password2']

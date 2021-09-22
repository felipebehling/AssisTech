from django.forms import ModelForm, fields
from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Relato

from .models import Account, relato


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Account
        # Campos que vão para o Register. (são do model Account em models.)
        fields = ['username', 'email', 'cpf', 'password1', 'password2']


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


# class relato_form(ModelForm):
#     class Meta:
#         model = relato
#         fields = "__all__"

#         def __init__(self, *args, **kwargs):
#             super(relato_form, self).__init__(*args, **kwargs)

#             for field in self.fields:
#                 self.fields[field].widget.attrs.update({'class': 'form-control'})

class relato_form(ModelForm):
    class Meta:
        model = Relato
        fields = ['id', 'nome', 'cpf', 'telefone', 'email', 'data_criacao', 'descricao', 'local', 'categoria']

    def __init__(self, *args, **kwargs):
        super(relato_form, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


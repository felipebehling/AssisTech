from django.forms import ModelForm, fields
from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Relato

from .models import Account, Relato


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

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username', 'email', 'profile_image', 'hide_email' )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


    def save(self, commit=True):
        account = super(AccountUpdateForm, self).save(commit=False)
        account.username = self.cleaned_data['username']
        account.email = self.cleaned_data['email'].lower()
        account.profile_image = self.cleaned_data['profile_image']
        account.hide_email = self.cleaned_data['hide_email']
        if commit:
            account.save()
        return account




class RelatoForm(ModelForm):
    class Meta:
        model = Relato
        fields = ['nome', 'cpf', 'telefone', 'email', 'data_criacao', 'descricao', 'local', 'categoria']
        
    def __init__(self, *args, **kwargs):
        super(RelatoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field]. widget.attrs.update({'class': 'form-control'})


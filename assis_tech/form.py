from django.forms import ModelForm
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

def __init__(self, *args, **kwargs):
    super(UsuarioForm, self).__init__(*args, **kwargs)
    self.fields['nome'].widget.attrs.update({'class': 'form-control'})
    self.fields['cpf'].widget.attrs.update({'class' : 'form-control'})
    self.fields['telefone'].widget.attrs.update({'class': 'form-control'})
    self.fields['email'].widget.attrs.update({'class': 'form-control'})
    self.fields['data_criacao'].widget.attrs.update({'class': 'form-control'})
    self.fields['descricao'].widget.attrs.update({'class': 'form-control'})



from django.contrib.auth.models import User
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from assis_tech.form import CreateUserForm, AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .form import relato_form
from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'pages/index.html')

def registerPage(request):
    context = {}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Usuário cadastrado com sucesso.')
            form.save()
        messages.add_message(request, messages.ERROR, 'Falha ao Registrar Usuário.')   


    return render(request, 'pages/register.html', context)

def loginPage(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')
        messages.add_message(request, messages.ERROR, 'Email ou Senha Inválido.')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'pages/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def report(request):
  return render(request, 'pages/report.html')


def form(request):
    data = {}
    data['form'] = relato_form()
    return render(request, 'pages/report.html', data)
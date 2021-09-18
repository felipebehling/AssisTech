
from django.contrib.auth.models import User
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from assis_tech.form import CreateUserForm, AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
        


    return render(request, 'pages/register.html', context)

def loginPage(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('index')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'pages/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

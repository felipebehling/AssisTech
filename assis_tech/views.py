
from django.contrib.auth.models import User
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'pages/index.html')

def registerPage(request):
    form = User

    if request.method == "POST":
        form = User(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Usuário cadastrado com sucesso.')
            form.save()

    context = {'form': form}

    return render(request, 'pages/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'pages/index.html')
        else:
            messages.info(request, 'CPF ou senha incorreta!' )
    context = {}
    return render(request, 'pages/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from assis_tech.form import CreateUserForm, AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .form import relato_form
from .models import Relato
from django.core.paginator import Paginator
from .filters import RelatoFilter
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def registerPage(request):
    context = {}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS,
                                 'Usuário cadastrado com sucesso.')
            form.save()
        messages.add_message(request, messages.ERROR,
                             'Falha ao Registrar Usuário.')

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
        messages.add_message(request, messages.ERROR,
                             'Email ou Senha Inválido.')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'pages/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def report(request):
    data = {}
    data['form'] = relato_form()
    return render(request, 'pages/report.html', data)


def relato_create(request):
    form = relato_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        print("- - - - - ")
        print(request.POST)


def dashboard(request):
    list_relatos = Relato.objects.order_by('id')
    myFilter = RelatoFilter(request.GET, queryset=list_relatos)
    list_relatos = myFilter.qs

    paginator = Paginator(list_relatos, 10)
    page = request.GET.get('page')
    list_relatos = paginator.get_page(page)
    return render(request, 'pages/dashboard.html', {'relatos': list_relatos, 'myFilter': myFilter})


def detail(request, pk):
    relato = Relato.objects.get(pk=pk)
    return render(request, 'pages/detalhe.html', {'relato': relato})


def edit(request, pk):
    relato = Relato.objects.get(pk=pk)
    form = relato_form(instance=relato)
    return render(request, 'pages/edit.html', {'relato': relato, 'form': form})


def update(request, pk):
    relato = Relato.objects.get(pk=pk)
    form = relato_form(request.POST, instance=relato)
    if form.is_valid():
        form.save()
        return redirect('dashboard')


def delete(request, pk):
    relato = Relato.objects.get(pk=pk)
    relato.delete()
    return redirect('dashboard')

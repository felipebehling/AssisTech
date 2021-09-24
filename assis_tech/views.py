
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from assis_tech.form import CreateUserForm, AccountAuthenticationForm, AccountUpdateForm
from django.contrib.auth import authenticate, login, logout
import folium

from .form import relato_form
from .models import Relato
from django.core.paginator import Paginator
from .filters import RelatoFilter

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from .models import Account

# Create your views here.


def index(request):
    # Create MAp
    m = folium.Map(location=[-26.900420999510086, -49.08161133527756], zoom_start=15)

    folium.Marker(location=[-26.900420999510086, -49.08161133527756], tooltop='clique para mais', popup='Centro POP').add_to(m)
    # Get html representation of map
    m = m._repr_html_()

    context = {
        'm': m,
    }
    return render(request, 'pages/index.html', context)

def registerPage(request):
    context = {}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS,
                                 'Usuário cadastrado com sucesso.')
            form.save()
        else:
          messages.add_message(request, messages.ERROR, 'Falha ao Registrar Usuário.')   

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

                return redirect('dashboard')
        messages.add_message(request, messages.ERROR, 'Email ou Senha Inválido.')

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



























  
def account_view(request, *args, **kwargs):
	"""
	- Logic here is kind of tricky
		is_self (boolean)
			is_friend (boolean)
				-1: NO_REQUEST_SENT
				0: THEM_SENT_TO_YOU
				1: YOU_SENT_TO_THEM
	"""
	context = {}
	user_id = kwargs.get("user_id")
	try:
		account = Account.objects.get(pk=user_id)
	except:
		return HttpResponse("Something went wrong.")
	if account:
		context['id'] = account.id
		context['username'] = account.username
		context['email'] = account.email
		context['profile_image'] = account.profile_image.url
		context['hide_email'] = account.hide_email

		# Define template variables
		is_self = True
		is_friend = False
		user = request.user
		if user.is_authenticated and user != account:
			is_self = False
		elif not user.is_authenticated:
			is_self = False
			
		# Set the template variables to the values
		context['is_self'] = is_self
		context['is_friend'] = is_friend
		return render(request, "pages/account.html", context)



def edit_account_view(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login")
	user_id = kwargs.get("user_id")
	account = Account.objects.get(pk=user_id)
	if account.pk != request.user.pk:
		return HttpResponse("You cannot edit someone elses profile.")
	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			new_username = form.cleaned_data['username']
			return redirect("account:view", user_id=account.pk)
		else:
			form = AccountUpdateForm(request.POST, instance=request.user,
				initial={
					"id": account.pk,
					"email": account.email, 
					"username": account.username,
					"profile_image": account.profile_image,
					"hide_email": account.hide_email,
				}
			)
			context['form'] = form
	else:
		form = AccountUpdateForm(
			initial={
					"id": account.pk,
					"email": account.email, 
					"username": account.username,
					"profile_image": account.profile_image,
					"hide_email": account.hide_email,
				}
			)
		context['form'] = form
	context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
	return render(request, "pages/edit_account.html", context)

























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

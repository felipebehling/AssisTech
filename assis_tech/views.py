from django.shortcuts import render
from .form import RelatoForm
from .models import Relato

# Create your views here.

def index(request):
  return render(request, 'pages/index.html')

def dashboard(request):
  list_relatos = Relato.objects.all()
  return render(request, 'pages/dashboard.html', {'relatos': list_relatos})


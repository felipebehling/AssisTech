import django_filters
from .models import Relato
from django_filters import CharFilter


class RelatoFilter(django_filters.FilterSet):
    nome = CharFilter(field_name='nome', lookup_expr='icontains')
    cpf = CharFilter(field_name="cpf", lookup_expr='icontains')
    class Meta:
        model = Relato
        fields = ['nome', 'cpf', 'categoria']

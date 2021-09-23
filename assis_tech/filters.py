import django_filters
from .models import Relato


class RelatoFilter(django_filters.FilterSet):
    class Meta:
        model = Relato
        fields = ['nome', 'cpf', 'categoria']

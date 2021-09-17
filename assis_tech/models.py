from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=250)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

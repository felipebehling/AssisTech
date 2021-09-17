from django.contrib import admin
from .models import Categoria, Relato
# Register your models here.

class RelatoAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "cpf", "telefone", "email", "categoria"]
    list_display_links = ["id"]
    list_editable = ["telefone", "email", "categoria"]

admin.site.register(Categoria)
admin.site.register(Relato, RelatoAdmin)

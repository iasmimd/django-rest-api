from django.contrib import admin

from .models import Endereco

admin.site.register(Endereco)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = ('linha1', 'linha2', 'cidade', 'estado', 'pais')
    search_fields = ('linha1')
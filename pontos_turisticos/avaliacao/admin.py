from django.contrib import admin

from .models import Avaliacao

admin.site.register(Avaliacao)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data', 'nota', 'aprovado')
    search_fields = ('usuario')
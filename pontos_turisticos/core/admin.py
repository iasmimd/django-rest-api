from django.contrib import admin
from .models import PontoTuristico

admin.site.register(PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'aprovado')
    search_fields = ('nome')
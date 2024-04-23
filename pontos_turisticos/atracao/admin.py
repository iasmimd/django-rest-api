from django.contrib import admin

from .models import Atracao

admin.site.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'horario_funcionamento')
    search_fields = ('nome')
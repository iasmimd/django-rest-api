from django.contrib import admin

from .models import Comentario

admin.site.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data', 'aprovado')
    search_fields = ('usuario')
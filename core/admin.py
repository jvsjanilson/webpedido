from django.contrib import admin
from core.models import Estado, Cidade


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('uf', 'nome')
    fields = ('uf', 'nome')


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    fields = ('nome', 'estado')


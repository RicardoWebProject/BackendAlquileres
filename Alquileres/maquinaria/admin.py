from django.contrib import admin
from .models import Maquinaria
# Register your models here.

@admin.register(Maquinaria)
class MaquinariaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'tipo', 'estado', 'precio',)
    list_filter = ('tipo', 'estado',)
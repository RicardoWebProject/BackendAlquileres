from django.contrib import admin
from .models import Alquiler
# Register your models here.

@admin.register(Alquiler)
class AdminAlquiler(admin.ModelAdmin):
    list_display=('owner', 'fecha_inicio', 'fecha_devolucion', 'maquinaria', 'total',)
    list_filter = ('fecha_inicio', 'fecha_devolucion',)
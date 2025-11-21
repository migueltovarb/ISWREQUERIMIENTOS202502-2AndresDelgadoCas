from django.contrib import admin
from .models import Movimiento

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'tipo', 'cantidad', 'motivo', 'usuario', 'fecha_movimiento']
    list_filter = ['tipo', 'fecha_movimiento']
    search_fields = ['producto__nombre', 'motivo']
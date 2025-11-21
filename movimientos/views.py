from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from .models import Movimiento
from productos.models import Producto

def lista_movimientos(request):
    # Obtener parámetros de búsqueda
    buscar = request.GET.get('buscar', '')
    tipo = request.GET.get('tipo', '')
    
    # Filtrar movimientos
    movimientos = Movimiento.objects.all().order_by('-fecha_movimiento')
    
    if buscar:
        movimientos = movimientos.filter(
            Q(producto__nombre__icontains=buscar) | 
            Q(motivo__icontains=buscar) |
            Q(usuario__icontains=buscar)
        )
    
    if tipo:
        movimientos = movimientos.filter(tipo=tipo)
    
    # Estadísticas
    total_entradas = movimientos.filter(tipo='ENTRADA').count()
    total_salidas = movimientos.filter(tipo='SALIDA').count()
    
    context = {
        'movimientos': movimientos,
        'buscar': buscar,
        'tipo_seleccionado': tipo,
        'total_entradas': total_entradas,
        'total_salidas': total_salidas,
    }
    
    return render(request, 'movimientos/lista_movimientos.html', context)
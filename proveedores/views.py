from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Proveedor

@login_required
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', {
        'proveedores': proveedores
    })

@login_required
def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedores/detalle_proveedor.html', {
        'proveedor': proveedor
    })
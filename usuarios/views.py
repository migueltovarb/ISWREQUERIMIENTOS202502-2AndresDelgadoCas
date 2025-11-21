from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cliente

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'usuarios/lista_clientes.html', {
        'clientes': clientes
    })

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        
        try:
            Cliente.objects.create(
                nombre=nombre,
                email=email,
                telefono=telefono,
                direccion=direccion
            )
            messages.success(request, 'Cliente creado exitosamente')
            return redirect('usuarios:lista_clientes')
        except Exception as e:
            messages.error(request, f'Error al crear cliente: {str(e)}')
    
    return render(request, 'usuarios/crear_cliente.html')

@login_required
def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'usuarios/detalle_cliente.html', {
        'cliente': cliente
    })
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Producto, Categoria
from proveedores.models import Proveedor
from .forms import ProductoForm

def lista_productos(request):
    # Obtener parámetros de búsqueda y filtro
    buscar = request.GET.get('buscar', '')
    categoria_id = request.GET.get('categoria', '')
    proveedor_id = request.GET.get('proveedor', '')
    
    # Filtrar productos
    productos = Producto.objects.all()
    
    if buscar:
        productos = productos.filter(
            Q(nombre__icontains=buscar) | 
            Q(codigo__icontains=buscar) |
            Q(descripcion__icontains=buscar)
        )
    
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    if proveedor_id:
        productos = productos.filter(proveedor_id=proveedor_id)
    
    # Obtener categorías y proveedores para los filtros
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.filter(activo=True)
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'proveedores': proveedores,
        'buscar': buscar,
        'categoria_seleccionada': categoria_id,
        'proveedor_seleccionado': proveedor_id,
    }
    
    return render(request, 'productos/lista_productos.html', context)

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.filter(activo=True)
    
    context = {
        'form': form,
        'categorias': categorias,
        'proveedores': proveedores,
        'modo': 'crear'
    }
    
    return render(request, 'productos/form_producto.html', context)

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.filter(activo=True)
    
    context = {
        'form': form,
        'producto': producto,
        'categorias': categorias,
        'proveedores': proveedores,
        'modo': 'editar'
    }
    
    return render(request, 'productos/form_producto.html', context)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('lista_productos')
    
    context = {
        'producto': producto
    }
    
    return render(request, 'productos/confirmar_eliminar.html', context)
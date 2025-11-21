from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import VehiculoForm
from .models import vehiculo

def create_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_vehiculos')
    else:
        form = VehiculoForm()
    
    return render(request, 'create_vehiculo.html', {'form': form})

def list_vehiculos(request):
    vehiculos = vehiculo.objects.all()
    return render(request, 'list_vehiculos.html', {'vehiculos': vehiculos})

def update_vehiculo(request, id):
    vehiculo_obj = get_object_or_404(vehiculo, id=id)
    
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo_obj)
        if form.is_valid():
            form.save()
            return redirect('list_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo_obj)
    
    return render(request, 'update_vehiculo.html', {'form': form})

def delete_vehiculo(request, id):
    vehiculo_obj = get_object_or_404(vehiculo, id=id)
    
    if request.method == 'POST':
        vehiculo_obj.delete()
        return redirect('list_vehiculos')
    
    return render(request, 'delete_vehiculo.html', {'vehiculo': vehiculo_obj})
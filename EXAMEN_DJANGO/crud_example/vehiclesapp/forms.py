from django import forms
from .models import vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = vehiculo
        fields = ['placa', 'marca', 'color', 'modelo']
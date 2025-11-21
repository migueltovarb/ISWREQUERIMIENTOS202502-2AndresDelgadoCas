from django import forms
from .models import Producto, Categoria
from proveedores.models import Proveedor

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'codigo', 'nombre', 'descripcion', 'categoria', 'proveedor',
            'precio_compra', 'precio_venta', 'stock_actual', 'stock_minimo', 'ubicacion'
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PROD-001'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del producto'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-control'
            }),
            'precio_compra': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'precio_venta': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'stock_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'stock_minimo': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'value': '5'
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Estante A-1'
            }),
        }
        labels = {
            'codigo': 'Código del Producto',
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'categoria': 'Categoría',
            'proveedor': 'Proveedor',
            'precio_compra': 'Precio de Compra ($)',
            'precio_venta': 'Precio de Venta ($)',
            'stock_actual': 'Stock Actual',
            'stock_minimo': 'Stock Mínimo',
            'ubicacion': 'Ubicación en Almacén',
        }
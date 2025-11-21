from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from proveedores.models import Proveedor
from productos.models import Producto
from movimientos.models import Movimiento
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta

@login_required
def dashboard(request):
    # Estadísticas para el dashboard
    total_productos = Producto.objects.count()
    total_proveedores = Proveedor.objects.count()
    productos_bajo_stock = Producto.objects.filter(stock_actual__lt=10).count() if hasattr(Producto, 'stock_actual') else 0
    
    # Productos que necesitan reabastecimiento
    productos_reabastecer = Producto.objects.filter(stock_actual__lt=10)[:5] if hasattr(Producto, 'stock_actual') else []
    
    # Movimientos recientes
    movimientos_recientes = Movimiento.objects.all().order_by('-fecha_movimiento')[:10] if hasattr(Movimiento, 'fecha_movimiento') else []
    
    context = {
        'total_productos': total_productos,
        'total_proveedores': total_proveedores,
        'productos_bajo_stock': productos_bajo_stock,
        'productos_reabastecer': productos_reabastecer,
        'movimientos_recientes': movimientos_recientes,
        'alertas_stock_bajo': productos_bajo_stock > 0
    }
    return render(request, 'reportes/dashboard.html', context)

@login_required
def administracion(request):
    total_usuarios = User.objects.count()
    total_proveedores = Proveedor.objects.count()
    total_productos = Producto.objects.count()
    
    return render(request, 'administracion/administracion.html', {
        'total_usuarios': total_usuarios,
        'total_proveedores': total_proveedores,
        'total_productos': total_productos
    })

@login_required
def reporte_productos(request):
    productos = Producto.objects.all()
    
    # Estadísticas de productos
    total_productos = productos.count()
    productos_activos = productos.filter(activo=True).count() if hasattr(Producto, 'activo') else total_productos
    productos_bajo_stock = productos.filter(stock_actual__lt=10).count() if hasattr(Producto, 'stock_actual') else 0
    
    return render(request, 'reportes/reporte_productos.html', {
        'productos': productos,
        'total_productos': total_productos,
        'productos_activos': productos_activos,
        'productos_bajo_stock': productos_bajo_stock
    })

@login_required
def reporte_movimientos(request):
    movimientos = Movimiento.objects.all().order_by('-fecha_movimiento')
    
    # Estadísticas de movimientos
    total_movimientos = movimientos.count()
    movimientos_entrada = movimientos.filter(tipo='ENTRADA').count() if hasattr(Movimiento, 'tipo') else 0
    movimientos_salida = movimientos.filter(tipo='SALIDA').count() if hasattr(Movimiento, 'tipo') else 0
    
    # Movimientos del último mes
    ultimo_mes = timezone.now() - timedelta(days=30)
    movimientos_ultimo_mes = movimientos.filter(fecha_movimiento__gte=ultimo_mes).count() if hasattr(Movimiento, 'fecha_movimiento') else 0
    
    return render(request, 'reportes/reporte_movimientos.html', {
        'movimientos': movimientos,
        'total_movimientos': total_movimientos,
        'movimientos_entrada': movimientos_entrada,
        'movimientos_salida': movimientos_salida,
        'movimientos_ultimo_mes': movimientos_ultimo_mes
    })

@login_required
def reporte_proveedores(request):
    proveedores = Proveedor.objects.all()
    
    # Estadísticas de proveedores
    total_proveedores = proveedores.count()
    proveedores_activos = proveedores.filter(activo=True).count()
    
    return render(request, 'reportes/reporte_proveedores.html', {
        'proveedores': proveedores,
        'total_proveedores': total_proveedores,
        'proveedores_activos': proveedores_activos
    })
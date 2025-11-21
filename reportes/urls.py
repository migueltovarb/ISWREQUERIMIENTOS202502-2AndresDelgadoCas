from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('administracion/', views.administracion, name='administracion'),
    path('reporte-productos/', views.reporte_productos, name='reporte_productos'),
    path('reporte-movimientos/', views.reporte_movimientos, name='reporte_movimientos'),
    path('reporte-proveedores/', views.reporte_proveedores, name='reporte_proveedores'),
]
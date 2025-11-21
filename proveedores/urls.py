from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('', views.lista_proveedores, name='lista_proveedores'),
    path('<int:pk>/', views.detalle_proveedor, name='detalle_proveedor'),
]
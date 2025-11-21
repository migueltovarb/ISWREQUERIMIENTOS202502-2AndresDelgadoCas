from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
]
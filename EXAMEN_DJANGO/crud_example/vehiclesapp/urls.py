from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_vehiculo, name='create_vehiculo'),
    path('update/<int:id>/', views.update_vehiculo, name='update_vehiculo'),
    path('delete/<int:id>/', views.delete_vehiculo, name='delete_vehiculo'),
    path('', views.list_vehiculos, name='list_vehiculos'),
]
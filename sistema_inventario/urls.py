from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/reportes/')),  # ← CAMBIADO de /dashboard/ a /reportes/
    path('productos/', include('productos.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('movimientos/', include('movimientos.urls')),
    path('reportes/', include('reportes.urls')),
    path('usuarios/', include('usuarios.urls')),
    # path('dashboard/', include('reportes.urls')),  # ← ESTA LÍNEA SE ELIMINA
    
    # URLs de autenticación
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
]
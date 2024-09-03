from AppCiberseguridad import views 
from django.urls import path


urlpatterns = [
    path('', views.padre , name='padre'), 
    path('producto/', views.Producto, name='producto'), 
    path('cliente/',views.Cliente , name='cliente'),
    path('opiniones/',views.Opiniones, name='opiniones'), 
    path('inicio/',views.Inicio , name='inicio' ) ,
    path('app-form/', views.app_form, name='AppForm'),
    path('busquedaCliente/', views.busquedaCliente, name='BusquedaCliente'),
    path('ruta-buscar/', views.buscar, name='buscar'),
    path('app-formproducto', views.app_formProducto, name='AppFormProducto'),
    path('app-formopiniones', views.app_formOpiniones, name='AppFormOpiniones')
 ]
 
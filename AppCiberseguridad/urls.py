from django.urls import path
from AppCiberseguridad import views
from AppCiberseguridad import views_clases


urlpatterns = [
    path('', views.padre, name='padre'), 
    path('producto/', views.Producto, name='producto'), 
    path('cliente/', views.Cliente, name='cliente'),
    path('opiniones/', views.Opiniones, name='opiniones'), 
    path('inicio/', views.Inicio, name='inicio'),
    path('app-form/', views.app_form, name='AppForm'),
    path('busquedaCliente/', views.busquedaCliente, name='BusquedaCliente'),
    path('ruta-buscar/', views.buscar, name='buscar'),
    path('app-formproducto/', views.app_formProducto, name='AppFormProducto'),
    path('app-formopiniones/', views.app_formOpiniones, name='AppFormOpiniones'),
    path('leerclientes/', views.leerCliente, name='leerClientes'),
    path('eliminarCliente/<cliente_nombre>/', views.eliminarCliente, name="EliminarCliente"),
    path('leeropinion/', views.leerOpinion, name='leerOpinion'),
    path('eliminarOpinion/<opinion_nombre>/', views.eliminarOpinion, name="EliminarOpinion"),
       
]

urls_vistas_clases = [
    path('clases/lista/', views_clases.OpinionesListView.as_view(), name='List'), 
    path('clases/detalle/<int:pk>/', views_clases.OpinionesDetailView.as_view(), name='Detail'),
    path('clases/nuevo/', views_clases.OpinionesCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>/', views_clases.OpinionesUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>/', views_clases.OpinionesDeleteView.as_view(), name='Delete'),
]


urlpatterns += urls_vistas_clases 
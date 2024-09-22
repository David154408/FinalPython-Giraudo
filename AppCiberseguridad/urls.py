from django.urls import path
from AppCiberseguridad import views
from AppCiberseguridad import views_clases
from django.conf import settings
from django.conf.urls.static import static


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
    path('clases/lista/', views_clases.OpinionesListView.as_view(), name='OpinionesList'), 
    path('clases/detalle/<int:pk>/', views_clases.OpinionesDetailView.as_view(), name='OpinionesDetail'),
    path('clases/nuevo/', views_clases.OpinionesCreateView.as_view(), name='OpinionesCreate'),
    path('clases/editar/<int:pk>/', views_clases.OpinionesUpdateView.as_view(), name='OpinionesEdit'),
    path('clases/eliminar/<int:pk>/', views_clases.OpinionesDeleteView.as_view(), name='OpinionesDelete'),
]

urlpatterns += urls_vistas_clases 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
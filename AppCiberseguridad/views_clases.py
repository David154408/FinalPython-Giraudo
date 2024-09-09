from django.shortcuts import render
from .models import Opiniones
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import  Opiniones, Producto
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Formularios de autenticación de usuarios
from django.contrib.auth import login, logout, authenticate  # Funciones para gestionar inicios de sesión y autenticación


def inicio(request):
    return render(request, "AppCiberseguridad/padre.htlm")

def about(request):
    return render(request,"AppCiberseguridad/about.htlm")
# Aca tenemos las vistas de  nuestro opiniones:

class OpinionesListView( ListView):
    model = Opiniones
    context_object_name = 'opiniones'
    template_name = 'AppCiberseguridad/Vistas_Clases/opiniones_list.html'

class OpinionesDetailView( DetailView):
    model = Opiniones
    context_object_name = 'opinion'
    template_name = 'AppCiberseguridad/Vistas_Clases/opiniones_detail.html'

class OpinionesCreateView(CreateView):
    model = Opiniones
    fields = ['nombre', 'descripcion']
    template_name = 'AppCiberseguridad/Vistas_Clases/opinion_form.html'
    success_url = reverse_lazy('opiniones_list')

class OpinionesUpdateView( UpdateView):
    model = Opiniones
    fields = ['nombre', 'descripcion']
    template_name = 'appciberseguridad/Vistas_clases/opinion_form.html'
    success_url = reverse_lazy('opiniones_list')

class OpinionesDeleteView( DeleteView):
    model = Opiniones
    template_name = 'AppCiberseguridad/Vistas_Clases/opinion_confirm_delete.html'
    success_url = reverse_lazy('opiniones_list')

# Aca tenemos las vistas de  nuestro productos: 

class ProductoListView( ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'AppCiberseguridad/Vistas_Clases/productos_list.html'

class ProductoDetailView( DetailView):
    model = Producto
    context_object_name = 'producto'
    template_name = 'AppCiberseguridad/Vistas_Clases/producto_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'AppCiberseguridad/Vistas_Clases/producto_form.html'
    success_url = reverse_lazy('productos_list')

class ProductoUpdateView( UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'AppCiberseguridad/Vistas_Clases/producto_form.html'
    success_url = reverse_lazy('productos_list')

class ProductoDeleteView( DeleteView):
    model = Producto
    template_name = 'AppCiberseguridad/producto_confirm_delete.html'
    success_url = reverse_lazy('productos_list')
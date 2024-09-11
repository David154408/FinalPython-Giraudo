from django.shortcuts import render
from .models import Opiniones
from .models import Producto 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import  Opiniones, Producto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required 

def inicio(request):
    return render(request, "AppCiberseguridad/padre.htlm")

def about(request):
    return render(request,"AppCiberseguridad/about.htlm")
# Aca tenemos las vistas de  nuestro opiniones:

class OpinionesListView(LoginRequiredMixin  ,ListView):
    model = Opiniones
    context_object_name = 'opiniones'
    template_name = 'AppCiberseguridad/Vistas_Clases/opiniones_list.html'
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class OpinionesDetailView(LoginRequiredMixin, DetailView):
    model = Opiniones
    context_object_name = 'opiniones'
    template_name = 'AppCiberseguridad/Vistas_Clases/opiniones_detail.html'
    success_url = reverse_lazy("OpinionesList") 
    
class OpinionesCreateView(LoginRequiredMixin,CreateView):
    model = Opiniones
    fields = ['nombre', 'descripcion']
    template_name = 'AppCiberseguridad/Vistas_Clases/opinion_form.html'
    success_url = reverse_lazy("OpinionesList")

class OpinionesUpdateView(LoginRequiredMixin, UpdateView):
    model = Opiniones
    fields = ['nombre', 'descripcion']
    template_name = 'appciberseguridad/Vistas_Clases/opinion_form.html'
    ssuccess_url = reverse_lazy("OpinionesList")

class OpinionesDeleteView(LoginRequiredMixin, DeleteView):
    model = Opiniones
    template_name = 'AppCiberseguridad/Vistas_Clases/opinion_confirm_delete.html'
    success_url = reverse_lazy("OpinionesList")

# Aca tenemos las vistas de  nuestro productos: 

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'AppCiberseguridad/Vistas_Clases/productos_list.html'

class ProductoDetailView( LoginRequiredMixin,DetailView):
    model = Producto
    context_object_name = 'producto'
    template_name = 'AppCiberseguridad/Vistas_Clases/producto_detail.html'

class ProductoCreateView(LoginRequiredMixin,CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'AppCiberseguridad/Vistas_Clases/producto_form.html'
    success_url = reverse_lazy("ProductoList")

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'AppCiberseguridad/Vistas_Clases/producto_form.html'
    success_url = reverse_lazy("ProductoList")

class ProductoDeleteView( LoginRequiredMixin,DeleteView):
    model = Producto
    template_name = 'AppCiberseguridad/Vistas_Clases/producto_confirm_delete.html'
    success_url = reverse_lazy("ProductoList")
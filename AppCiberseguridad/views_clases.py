from django.shortcuts import render
from .models import Opiniones
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import  Opiniones, Producto
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Formularios de autenticación de usuarios
from django.contrib.auth import login, logout, authenticate  # Funciones para gestionar inicios de sesión y autenticación


def login_request(request):
    """
    Función para manejar las solicitudes de inicio de sesión.
    """
    if request.method == "POST":  # Si el formulario fue enviado (método POST)
        form = AuthenticationForm(request, data=request.POST)  # Crea un formulario y lo llena con los datos enviados
        print(form)  # Imprime el formulario en la consola (para depuración)

        if form.is_valid():  # Si el formulario es válido
            usuario = form.cleaned_data.get("username")  # Obtiene el nombre de usuario
            clave = form.cleaned_data.get("password")  # Obtiene la contraseña

            nombre_usuario = authenticate(username=usuario, password=clave)  # Intenta autenticar al usuario

            if nombre_usuario is not None:  # Si la autenticación es exitosa
                login(request, nombre_usuario)  # Inicia la sesión del usuario
                return render(request, "AppCiberseguridad/padre.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})  # Renderiza la plantilla con un mensaje de bienvenida
            else:  # Si la autenticación falla
                form = AuthenticationForm()  # Crea un nuevo formulario vacío
                return render(request, "AppCiberseguridad/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  # Renderiza el formulario de login con un mensaje de error
        else:  # Si el formulario no es válido
            return render(request, "AppCiberseguridad/padre.html", {"mensaje":"Error, formulario inválido"})  # Renderiza la plantilla con un mensaje de error

    form = AuthenticationForm()  # Si es una solicitud GET (primera vez que se accede a la página), crea un formulario vacío
    return render(request, "AppCiberseguridad/login.html", {"form":form})  # Renderiza el formulario de login



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
    template_name = 'AppCiberseguridad/Vistas_Clases/producto_confirm_delete.html'
    success_url = reverse_lazy('productos_list')
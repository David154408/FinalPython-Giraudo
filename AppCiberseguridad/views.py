from django.http import HttpResponse
from django.shortcuts import render 
from AppCiberseguridad.models import Cliente as ClienteModel
from AppCiberseguridad.models import Producto as ProductoModel
from AppCiberseguridad.models import Opiniones as OpinionesModel 
## from .models import Opiniones
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'AppCiberseguridad/index.html')

def padre(req):
    return render(req, 'AppCiberseguridad/padre.html')
    
    
def Inicio(req):
    return render(req, 'AppCiberseguridad/index.html')


def Producto(req):
    return render(req, 'AppCiberseguridad/producto.html')

@login_required
def Cliente(req):
  return render(req, 'AppCiberseguridad/cliente.html')

@login_required
def Opiniones(req):
    return render(req, 'AppCiberseguridad/opiniones.html')


### def app_form , es el formulario para agragar clientes a la base de datos ! 
def app_form(req):
        
    if req.method == 'POST':
        
        cliente = ClienteModel(
            nombre=req.POST['nombre'] ,
            correo_electronico=req.POST['correo_electronico'], 
            telefono=req.POST['telefono'],
            direccion=req.POST['direccion'] 
            )
        
        cliente.save()
        return render(req,"AppCiberseguridad/padre.html")
       
    return render(req , 'AppCiberseguridad/appFormulario.html')


def app_formProducto(req):
    if req.method == 'POST':
        
        producto= ProductoModel(
            nombre=req.POST['nombre'] ,
            descripcion=req.POST['descripcion'],
            precio=req.POST['precio']
            )
        producto.save()
        return render(req, "AppCiberseguridad/padre.html")
       
    return render(req, 'AppCiberseguridad/appFormularioProducto.html')

def app_formOpiniones(req):
    if req.method == 'POST' :
        opiniones = OpinionesModel(
            nombre=req.POST['nombre'] ,
            descripcion=req.POST['descripcion']
            ) 
        opiniones.save()
        return render ( req, "AppCiberseguridad/padre.html")
    
    return render (req , 'AppCiberseguridad/appFormularioOpiniones.html')
    
def busquedaCliente(request) :
    return render(request, "AppCiberseguridad/busquedaCliente.html")

    
def buscar(request):
    cliente_nombre = request.GET.get('cliente')
    
    if cliente_nombre:
        resultados = ClienteModel.objects.filter(nombre__icontains=cliente_nombre)
    else:
        resultados = []
    
    return render(request, 'AppCiberseguridad/resultadoBusqueda.html', {
        'cliente_nombre': cliente_nombre,
        'resultados': resultados,
    })

def leerCliente(req):
    clientes=ClienteModel.objects.all() 
    contexto= {"clientes":clientes}
    return render (req, "AppCiberseguridad/leerCLientes.html",contexto) 
    
def eliminarCliente(req, cliente_nombre):
    cliente= ClienteModel.objects.get(nombre=cliente_nombre)
    cliente.delete()
    
    clientes= ClienteModel.objects.all() 
    
    contexto={"clientes":clientes}
    
    return render(req, "AppCiberseguridad/leerCLientes.html",contexto ) 

def leerOpinion(req):
    opiniones=OpinionesModel.objects.all()
    contexto={"opiniones":opiniones}
    return render (req, 'AppCiberseguridad/leerOpinion.html', contexto)

def eliminarOpinion(req, opinion_nombre):
    opinion=OpinionesModel.objects.get(nombre=opinion_nombre)
    opinion.delete()
    
    opiniones= OpinionesModel.objects.all()
    contexto={"opiniones": opiniones}

    
    return render(req,"AppCiberseguridad/leerOpinion.html", contexto) 
   

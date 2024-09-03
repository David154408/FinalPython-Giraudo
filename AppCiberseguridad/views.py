from django.http import HttpResponse
from django.shortcuts import render
from AppCiberseguridad.models import Cliente as ClienteModel
from AppCiberseguridad.models import Producto as ProductoModel
from AppCiberseguridad.models import Opiniones as OpinionesModel 
# Create your views here.

def padre(req):
    return render(req, 'AppCiberseguridad/padre.html')
    
    
def Inicio(req):
    return render(req, 'AppCiberseguridad/index.html')

def Producto(req):
    return render(req, 'AppCiberseguridad/producto.html')

def Cliente(req):
  return render(req, 'AppCiberseguridad/cliente.html')

def Opiniones(req):
    return render(req, 'AppCiberseguridad/opiniones.html')


### def app_form , es el formulario para agragar clientes a la base de datos ! 
def app_form(req):
        
    if req.method == 'POST':
        
        cliente = ClienteModel(
            nombre=req.POST['nombre'] ,
            correo_electronico=req.POST['correo_electronico'], 
            telefono=req.POST['telefono'] 
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

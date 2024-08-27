from django.http import HttpResponse
from django.shortcuts import render
from AppCiberseguridad.models import Cliente as ClienteModel
# Create your views here.

def Inicio(req):
    return render(req, 'AppCiberseguridad/padre.html')

def Producto(req):
    return render(req, 'AppCiberseguridad/producto.html')

def Cliente(req):
  return render(req, 'AppCiberseguridad/cliente.html')

def Opiniones(req):
    return render(req, 'AppCiberseguridad/opiniones.html')

def app_form(req):
        
    if req.method == 'POST':
        
        cliente = ClienteModel(
            nombre=req.POST['nombre'] ,
            correo_electronico=req.POST['correo_electronico'], 
            telefono=req.POST['telefono'] 
            )
        
        cliente.save()
        return render(req,"AppCiberseguridad/index.html")
       
    return render(req , 'AppCiberseguridad/appFormulario.html')


def busquedaCliente(request) :
    return render(request, "AppCiberseguridad/busquedaCliente.html")

def buscar(request):
    
    cliente_nombre = request.GET.get('cliente')
    
    if cliente_nombre:
        respuesta = f"Estoy buscando el cliente: {cliente_nombre}"
    else:
        respuesta = "No se ha proporcionado un nombre de cliente."

    # Retornar la respuesta como una instancia de HttpResponse
    return HttpResponse(respuesta)



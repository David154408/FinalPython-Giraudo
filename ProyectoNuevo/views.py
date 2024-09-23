from django.http import HttpResponse 
from django.template import loader 
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Profes  ")

def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")

def probando_plantilla(request):
    
    nom= "Jonathan"
    ap= "Giraudo"
    
    diccionario= { "nombre": nom, "apellido": ap, }
    
    plantilla = loader.get_template('template1.html')
    documento= plantilla.render(diccionario)
    
    return HttpResponse(documento)

def home(request):
    return render(request, 'AppCiberseguridad/index.html')
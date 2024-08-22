from django.http import HttpResponse 

def saludo(request):
    return HttpResponse("Hola Profes  ")

def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")
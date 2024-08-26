from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.CharField(max_length=150) 
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    
  
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField() 
    telefono = models.CharField(max_length=15)  
    direccion = models.TextField(blank=True)  

class Opiniones(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.CharField(max_length=1000) 

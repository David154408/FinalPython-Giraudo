from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.CharField(max_length=150) 
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion : {self.descripcion} - Precio: {self.precio}" 
  
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField() 
    telefono = models.CharField(max_length=15)  
    direccion = models.TextField(max_length=15) 
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Correo_Electronico: {self.correo_electronico} - Telefono : {self.telefono} - Direcccion: {self.direccion}"
    
    
class Opiniones(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.CharField(max_length=1000) 

    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion: {self.descripcion}" 
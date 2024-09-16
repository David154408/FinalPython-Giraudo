from django import forms
from .models import Producto
from .models import Opiniones

class Buscar(forms.Form):
    nombre=forms.CharField(max_length=20)
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

class OpinionesForm(forms.ModelForm):
    class Meta:
        
        model= Opiniones
        fields= ['nombre', 'descripcion']
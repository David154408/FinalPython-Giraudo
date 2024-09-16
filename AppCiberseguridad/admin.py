from django.contrib import admin
from AppCiberseguridad.models import Producto ,Cliente ,Opiniones 
from .models import * 
# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Opiniones)

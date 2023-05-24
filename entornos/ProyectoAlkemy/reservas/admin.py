from django.contrib import admin
from reservas.models import *



class ClienteAdmin(admin.ModelAdmin):
    cliente = Cliente
    list_display = ("id", "nombre", "apellido", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("activo")
    
class ServicioAdmin(admin.ModelAdmin):
    servicio = Servicio
    list_display = ("id", "nombre", "descripcion", "activo")
    search_fields = ("nombre")
    list_filter = ("activo" )
    
class EmpleadoAdmin(admin.ModelAdmin):
    empleado = Empleado
    list_display = ("id", "nombre", "apellido", "numero_legajo", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("activo" )
    
class CoordinadorAdmin(admin.ModelAdmin):
    coordinaro = Coordinador
    list_display = ("id", "nombre", "apellido", "dni", "fecha_alta", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("activo" )
    

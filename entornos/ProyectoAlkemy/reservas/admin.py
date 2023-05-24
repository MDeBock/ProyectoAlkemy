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

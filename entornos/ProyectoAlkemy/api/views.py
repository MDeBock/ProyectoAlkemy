from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from reservas.models import Servicio
from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
# Create your views here.

def inicio(request):
    return HttpResponse("Hola")

def servicios_listado(request):
    servicios = Servicio.objects.values('id','nombre','precio')
    
    return JsonResponse(list(servicios),safe=False);

def servicio_por_id(request,id_servicio):
    try:
        
        servicio = Servicio.objects.get(id=id_servicio)
        servicio_json = { 
            'id': servicio.id,
            'nombre': servicio.nombre,
            'precio': servicio.precio
        }

    except ObjectDoesNotExist:

        servicio_json = []

    return JsonResponse(servicio_json, safe=False)


    

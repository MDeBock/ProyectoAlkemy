from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest
from reservas.models import Servicio,Coordinador,Cliente,Empleado
from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
# Create your views here.

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
        return JsonResponse(servicio_json, safe=False)
    except ObjectDoesNotExist:

        servicio_json = []
        respuesta = JsonResponse(servicio_json, safe=False)
        respuesta.status_code=404
        #JsonResponse.status_code=400;
        return respuesta
        #return HttpResponse(content=servicio_json, content_type="status=status.HTTP_200_OK")
    
    

def coordinadores_listado(request):
    coordinadores=Coordinador.objects.values();

    return JsonResponse(list(coordinadores),safe=False);
    
def clientes_listado(request):
    clientes=Cliente.objects.values();

    return JsonResponse(list(clientes),safe=False)

def empleados_listado(request):
    empleados=Empleado.objects.values();

    return JsonResponse(list(empleados),safe=False)
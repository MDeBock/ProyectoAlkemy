from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado

# Create your views here.
def index(request):

    return HttpResponse("Hola mundo")

def registrar_empleado(request):

    if request.method == "POST":

        Empleado.objects.create(
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
            numero_legajo = request.POST["numero_legajo"],
        );
        
    return render(request,'reservas/registrar_empleado.html');


def activar_empleado(request,id_empleado):
  
    empleado=Empleado.objects.get(id=id_empleado);
    empleado.activo=True;
    empleado.save();

    return HttpResponse(f"Se activo el cliente {empleado.nombre} {empleado.apellido}");   
 
 
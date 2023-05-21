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

    return HttpResponse(f"Se activo el empleado {empleado.nombre} {empleado.apellido}");   

def listado_empleados(request):
    empleados = Empleado.objects.all()
    context = {
        "empleados": empleados
    }
    return render(request, "reservas/listar_empleados.html", context)

def modificar_empleado(request, id_empleado):    
    empleado=Empleado.objects.get(id=id_empleado)    
    context = {
        "empleado": empleado
    }
    if request.POST:        
        nombre = request.POST["nombre"],
        apellido = request.POST["apellido"],
        numero_legajo = request.POST["numero_legajo"],
        
        empleado.nombre = nombre
        empleado.apellido = apellido
        empleado.numero_legajo = numero_legajo
        empleado.save()
          
    return render(request, "reservas/modificar_empleado.html", context)

def desactivar_empleado(request,id_empleado):
      
    empleado=Empleado.objects.get(id=id_empleado)
    empleado.activo=False
    empleado.save()

    return HttpResponse(f"El empleado {empleado.nombre} {empleado.apellido} se desactivo correctamente")
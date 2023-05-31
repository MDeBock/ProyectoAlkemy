from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado, Cliente, Coordinador, Servicio, ReservaServicio
from django.shortcuts import get_object_or_404,redirect
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

    return redirect('listado_empleados')

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
        
        empleado.nombre = nombre[0]
        empleado.apellido = apellido[0]
        empleado.numero_legajo = int(numero_legajo[0])
        empleado.save()
          
    return render(request, "reservas/modificar_empleado.html", context)

def desactivar_empleado(request,id_empleado):
      
    empleado=Empleado.objects.get(id=id_empleado)
    empleado.activo=False
    empleado.save()

    return redirect('listado_empleados')

def listado_clientes(request):
    clientes = Cliente.objects.all()
    context = {
        "clientes": clientes
    }
    return render(request, "reservas/listar_clientes.html", context)

def registrar_cliente(request):

    if request.POST:

        Cliente.objects.create(
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
        )
        
    return render(request,'reservas/registrar_cliente.html')

def registrar_coordinador(request):

    if request.POST:

        Coordinador.objects.create(
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
            numero_documento = request.POST["numero_documento"],
            fecha_alta = request.POST["fecha_alta"],
            activo = request.POST["activo"],
        )
        
    return render(request,'reservas/registrar_coordinador.html')

def modificar_coordinador(request,id_coordinador):

    coordinador = get_object_or_404(Coordinador, id=id_coordinador)
    #Se pasa el campo del modelo de tipo datetime a string para que se puede ver en el inpu correctamente
    coordinador.fecha_alta = coordinador.fecha_alta.strftime('%Y-%m-%d %H:%M:%S')

    if request.method == "POST":        
        coordinador.nombre = request.POST["nombre"];
        coordinador.apellido = request.POST["apellido"];
        coordinador.numero_documento = request.POST["numero_documento"];
        coordinador.fecha_alta = request.POST["fecha_alta"]
        coordinador.save();
    
    return render(request,'reservas/modificar_coordinador.html',{"coordinador": coordinador})

def activar_coordinador(request,id_coordinador):
      
    coordinador = Coordinador.objects.get(id=id_coordinador)
    coordinador.activo = True
    coordinador.save()
    return redirect('listado_coordinadores')

def desactivar_coordinador(request,id_coordinador):
      
    coordinador = Coordinador.objects.get(id=id_coordinador)
    coordinador.activo = False
    coordinador.save()
    return redirect('listado_coordinadores')

def desactivar_cliente(request,id_cliente):

    cliente = get_object_or_404(Cliente,id=id_cliente)
    if cliente.activo:
       cliente.activo=False
       cliente.save()
    
    return redirect('listado_clientes')

def activar_cliente(request,id_cliente):

    cliente = get_object_or_404(Cliente,id=id_cliente)
    if not cliente.activo:
       cliente.activo=True
       cliente.save()

    return redirect('listado_clientes')

def modificar_cliente(request,id_cliente):

    cliente = get_object_or_404(Cliente, id=id_cliente);
    if request.method == "POST":
        cliente.nombre = request.POST["nombre"]
        cliente.apellido = request.POST["apellido"]
        cliente.save();
    
    return render(request,'reservas/modificar_cliente.html',{"cliente":cliente})

def listado_coordinadores(request):
    coordinadores = Coordinador.objects.all()
    context = {
        "coordinadores": coordinadores
    }
    return render(request, "reservas/listar_coordinador.html", context)

def registrar_coordinador(request):

    if request.POST:

        Coordinador.objects.create(
            nombre = request.POST["nombre"],
            apellido = request.POST["apellido"],
            numero_documento = request.POST["numero_documento"],
            fecha_alta = request.POST["fecha_alta"],            
        )
        
    return render(request,'reservas/registrar_coordinador.html')

def registrar_reserva_de_servicio(request):

    clientes=Cliente.objects.filter(activo=True)
    responsables=Coordinador.objects.filter(activo=True)
    empleados=Empleado.objects.filter(activo=True)
    contexto={
        "clientes":clientes,
        "responsables":responsables,
        "empleados" : empleados
    }
    if request.method == "POST":
        pass

    print(f"contexto = {contexto}")

    return render(request, "reservas/registrar_reserva_de_servicio.html",contexto)

def modificar_reserva_de_servicio(request,id_reserva_servicio):
    
    reserva_servicio = get_object_or_404(ReservaServicio,id=id_reserva_servicio)
    
    clientes = Cliente.objects.filter(activo=True)
    responsables = Coordinador.objects.filter(activo=True)
    empleados = Empleado.objects.filter(activo=True)
    contexto = {
        "reserva_servicio": reserva_servicio,
        "clientes": clientes,
        "responsables": responsables,
        "empleados": empleados
    }
    if request.method == "POST":
        pass

    return render(request,"reservas/modificar_reserva_de_servicio.html",contexto)


def eliminar_reserva_de_servicio(request,id_reserva_servicio):
    
    reserva_servicio = get_object_or_404(ReservaServicio,id=id_reserva_servicio)
    reserva_servicio.delete()
    
    return HttpResponse(f"Se elimino el servicio {id_reserva_servicio} correctamente");
    #return redirect('listado_reservas_de_servicio')

def listado_reservas_de_servicios(request):

    reservas = ReservaServicio.objects.all();

    return render(request,"reservas/listar_reservas_de_servicios.html",{"reservas":reservas})
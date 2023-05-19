from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=50)
    apellido = models.CharField(verbose_name="Apellido",max_length=50)
    numero_legajo = models.IntegerField(verbose_name="Numero de legajo")
    activo = models.BooleanField(verbose_name="Activo",default=True)

class Coordinador(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=50)
    apellido = models.CharField(verbose_name="Apellido",max_length=50)
    numero_documento = models.IntegerField(verbose_name="Numero de documento")
    fecha_alta = models.DateTimeField(verbose_name="Fecha de alta")
    activo = models.BooleanField(verbose_name="Activo",default=True)

class Cliente(models.Model):
    nombre = models.CharField(verbose_name="Nombre",max_length=50)
    apellido = models.CharField(verbose_name="Apellido",max_length=50)
    activo = models.BooleanField(verbose_name="Activo",default=True)

class Servicio(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=50)
    precio = models.IntegerField(verbose_name="Precio")
    activo = models.BooleanField(verbose_name="Activo", default=True)

class ReservaServicio(models.Model):
    fecha_creacion = models.DateTimeField(verbose_name="Fecha de creacion")
    fecha_reserva = models.DateTimeField(verbose_name="Fecha de reserva")
    cliente = models.ForeignKey(Cliente,verbose_name="Cliente",on_delete=models.CASCADE,related_name="cliente")
    responsable = models.ForeignKey(Coordinador,verbose_name="Coordinador",on_delete=models.CASCADE,related_name="coordinador")
    empleado = models.ForeignKey(Empleado,verbose_name="Empleado",on_delete=models.CASCADE,related_name="empleado")
    servicio = models.ForeignKey(Servicio,verbose_name="Servicio",on_delete=models.CASCADE,related_name="servicio")
    precio = models.IntegerField(verbose_name="Precio")
    

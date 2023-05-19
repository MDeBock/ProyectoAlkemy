from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('empleados/crear/',views.registrar_empleado,name="registrar_empleado"),
    path('empleados/activar/<int:id_empleado>',views.activar_empleado, name="activar_empleado")
]
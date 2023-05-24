from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('empleados/crear/',views.registrar_empleado,name="registrar_empleado"),
    path('empleados/activar/<int:id_empleado>',views.activar_empleado, name="activar_empleado"),
    path('empleados/listar/', views.listado_empleados, name="listado_empleados"),
    path('empleados/modificar/<int:id_empleado>', views.modificar_empleado, name='modificar_empleado'),
    path('empleados/desactivar/<int:id_empleado>',views.desactivar_empleado, name="desactivar_empleado"),
    path('clientes/listado/', views.listado_clientes, name="listado_clientes"),
    path('clientes/nuevo/',views.registrar_cliente,name="registrar_cliente"),
    path('coordinadores/modificar/<int:id_coordinador>',views.modificar_coordinador,name="modificar_coordinador"),
    path('coordinadores/activar/<int:id_coordinador>',views.activar_coordinador,name="activar_coordinador"),
]
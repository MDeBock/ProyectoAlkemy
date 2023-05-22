from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('empleados/crear/',views.registrar_empleado,name="registrar_empleado"),
    path('empleados/activar/<int:id_empleado>',views.activar_empleado, name="activar_empleado"),
    path('empleados/listar/', views.listado_empleados, name="listado_empleados"),
    path('empleados/modificar/<int:id_empleado>', views.modificar_empleado, name='modificar_empleado'),
    path('empleados/desactivar/<int:id_empleado>',views.desactivar_empleado, name="desactivar_empleado"),
]
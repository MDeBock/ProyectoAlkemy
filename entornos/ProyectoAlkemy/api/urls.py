from django.urls import path, include
from . import views

urlpatterns = [
    path('servicios/',views.servicios_listado,name="servicios_listado"),
    path('servicios/<int:id_servicio>', views.servicio_por_id,name="servicio_por_id"),
    path('coordinadores/', views.coordinadores_listado,name="coordinadores_listado"),
    path('clientes/',views.clientes_listado,name="clientes_listado"),
    path('empleados/', views.empleados_listado, name="empleados_listado")
]

from django.urls import path, include
from . import views
urlpatterns = [
    path('servicios/',views.listado_servicios,name="listado_servicios"),
    path('servicios/<int:id_servicio>', views.servicio_por_id,name="servicio_por_id")
]

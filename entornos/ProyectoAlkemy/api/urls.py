from django.urls import path, include
from . import views
urlpatterns = [
    path('servicios/',views.servicios_listado,name="servicios_listado"),
    path('servicios/<int:id_servicio>', views.servicio_por_id,name="servicio_por_id")
]

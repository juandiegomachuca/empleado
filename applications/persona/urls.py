from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('',
        views.InicioView.as_view(),
        name='inicio'),    
        
    path('prueba_per/',views.pruebaPersona.as_view()),
    
    path(
        'persona/',
        views.ListAllEmpleados.as_view(),
        name='empleados_all'
    ),
    
    path(
        'buscar_persona/<busper>',
        views.EmpleadosByArea.as_view(),
        name='bus_per'
        ),
    
    path(
        'lista-empleados-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name='empleados_admin'
        ),
    
    path(
        'persona_by_area/<shorname>',
        views.ListByAreaEmpleado.as_view(),
        name='empleados_area'
        ),
    
    path(
        'crear_persona/',
        views.CrearPersona.as_view(),
        name="crear_persona"),
    
    path('ok/',
        views.OperacionExitosa.as_view(), 
        name='correcto'
    ),
    
    path('detalle_emp/<pk>',
        views.EmpleadoDetailView.as_view(),
        name='emp_det'
        ),

    path('modif_empl/<pk>/',
        views.PersonaUpdateView.as_view(),
        name='modif_empl'),

    path('borrar_empl/<pk>/',
        views.PersonaDeleteView.as_view(),
        name='borrar_empl'),
]

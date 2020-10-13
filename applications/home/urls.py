from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prueba/',views.pruebaVista.as_view()),
    path('lista/',views.pruebaListView.as_view()),
    path('listapru/',views.ListarPrueba.as_view()),
    path('add/',views.CrearPrueba.as_view()),
    path(
        'resumen/',
        views.ResumenFoundationView.as_view(),
        name='resu'
    ),
]

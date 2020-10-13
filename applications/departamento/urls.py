from django.contrib import admin
from django.urls import path

from . import views


app_name = "depto_app"

urlpatterns = [
    path(
        'deptos/',
        views.ListAllDep.as_view(),
        name='deptos'
        ),

    path(
        'nuevo_dep/',
        views.NewDepartamentoView.as_view(),
        name='nuevo_dep_per'),
]

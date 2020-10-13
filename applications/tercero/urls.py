from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('terceros/<depto>/',views.ListarTerceros.as_view()),
    path('terceros/',views.ListarTerceros.as_view()),
]

from django.shortcuts import render

# Create your views here.
from django.views.generic import (
        TemplateView, 
        ListView, 
        CreateView
)
# from persona.models import Persona, Habilidades
from .models import Tercero


class ListarTerceros(ListView):
    template_name = 'tercero/list_all.html'
    # model = 'Persona'
    context_object_name = 'lista'
    model = Tercero

    # def get_queryset(self):
    #     depto=self.kwargs['depto']
    #     lista = Tercero.objects.filter(
    #         departamento=depto
    # )
    #     return lista

    # def get_queryset(self):
    #     depto=self.kwargs['depto']
    #     lista = Tercero.objects.filter(
    #         departamento=depto
    # )
    #     return lista



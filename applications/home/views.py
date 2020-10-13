from django.shortcuts import render

from django.views.generic import (
        TemplateView, 
        ListView, 
        CreateView
)

from .models import Prueba
from django.urls import reverse_lazy
from .forms import PruebaForm

# Create your views here.

class pruebaVista(TemplateView):
    template_name = 'home/prueba.html'


class pruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['1','22','33']

class ListarPrueba(ListView):
    template_name = "home/listapru.html"
    model = Prueba
    context_object_name = 'lista'

class CrearPrueba(CreateView):
    template_name = "home/add.html"
    model = Prueba
    # fields = ['titulo','subtitulo','cantidad','valor']
    form_class = PruebaForm
    success_url = reverse_lazy("persona_app:correcto")


class ResumenFoundationView(TemplateView):
    template_name = "home/resumen_foundation.html"

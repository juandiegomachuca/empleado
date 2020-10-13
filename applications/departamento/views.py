from django.shortcuts import render

# Create your views here.
from django.views.generic import (
        ListView
)
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


from .models import Departamento
from .forms import NewDepartamentoForm

from applications.persona.models import Persona

class ListAllDep(ListView):
    template_name = 'departamento/list_all.html'
    model = Departamento
    context_object_name = 'lista'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_depto.html'
    form_class = NewDepartamentoForm
    # success_url = reverse_lazy("persona_app:correcto")
    success_url = reverse_lazy("persona_app:empleados_all")

    def form_valid(self, form):
        # lógica del proceso: vamos a sobreescribir el resultado
        # recuperar todo lo que está en la página aquí:
        # datos = form.save()
        # print(datos)
        # datos.nombre_completo=datos.first_name + ' ' + datos.last_name
        # datos.save #para que lo vuelva a guardar en la base de datos (no recomendado)
        depa=Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']

        perso=Persona(
            first_name = form.cleaned_data['nombre'],
            last_name = form.cleaned_data['apellidos'],
            nombre_completo = form.cleaned_data['nombre'] + ' ' + form.cleaned_data['apellidos'],
            job = 'CON',
            departamento = depa
        )
        perso.save()

        print('***** estamos en form_valid ****')
        print(nombre)
        print(apellidos)
        # return super(NewDepartamentoView,self).form_valid(form)
        return super().form_valid(form)    



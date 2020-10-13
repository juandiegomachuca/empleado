from django.shortcuts import render

# Create your views here.
from django.views.generic import (
        TemplateView, 
        ListView, 
        CreateView,
        DetailView,
        UpdateView,
        DeleteView
)
from django.urls import reverse_lazy
from .models import Persona, Habilidades
from applications.departamento.models import Departamento

# forms
from .forms import PersonaForm

class InicioView(TemplateView):
    template_name = "inicio.html"

class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = "persona/detalle.html"
    context_object_name = 'lista'
    
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # context['titulo']='Soy el mejor'
        # context['titulo2']='y tu?'
        print('**************** contex:')
        print(context)
        return context
    
    # def get_queryset(self):
    #     idempleado=self.kwargs['pk']
    #     lista = Persona.objects.filter(
    #         id=idempleado
    # )
    #     return lista


class pruebaPersona(ListView):
    template_name = "persona/list_all2.html"
    context_object_name = 'listaNumeros'
    model = Persona


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    # model = Persona
    context_object_name = 'lista'
    ordering = 'first_name'
    paginate_by = 4


    def get_queryset(self):
        buscar=self.request.GET.get('busper','')

        lista = Persona.objects.filter(
            first_name__icontains=buscar
        )

        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    # model = Persona
    context_object_name = 'lista'
    paginate_by = 10
    ordering = 'first_name'
    model = Persona


class BuscarPersona(ListView):
    template_name = 'persona/buscar_persona.html'
    context_object_name = 'lista'

    def get_queryset(self):
        print('******************************')
        buscar=self.request.GET.get('busper','')
        print('===============',buscar)

        lista = Persona.objects.filter(
            first_name=buscar
    )

        return lista

class EmpleadosByArea(ListView):
    template_name = 'persona/buscar_persona.html'
    context_object_name = 'lista'
    
    def get_queryset(self):
        buscar=self.request.GET.get('busper','')

        # lista = Persona.objects.filter(
        #     departamento__shor_name=buscar
        print('************** buscar:' + buscar + '***************')
        lista = Persona.objects.filter(
            first_name=buscar
        )
        return lista

class ListByAreaEmpleado(ListView):
    template_name = 'persona/buscar_persona.html'
    context_object_name = 'lista'
    model = Persona
    
    # def get_queryset(self):
    #     area = self.kwargs('shorname')
    #     lista = Persona.objects.filter(
    #         departamento__shor_name=area
    #     )
    #     print ('************ lista *******')
    #     print(lista)
    #     return lista



class CrearPersona(CreateView):
    model = Persona
    template_name = 'persona/add.html'
    context_object_name = 'lista'

    # cambiamos la forma de personalizar los formularios
    # fields = [
    #     'first_name',
    #     'last_name',
    #     'departamento',
    #     'job',
    #     'avatar',
    #     'anulate',
    #     'habilidades',
    #     'hoja_vida'
    # ]
    form_class = PersonaForm
    success_url = reverse_lazy("persona_app:empleados_all")

    def form_valid(self, form):
        # lógica del proceso: vamos a sobreescribir el resultado
        # recuperar todo lo que está en la página aquí:
        datos = form.save()
        print(datos)
        datos.nombre_completo=datos.first_name + ' ' + datos.last_name
        datos.save #para que lo vuelva a guardar en la base de datos (no recomendado)
        return super(CrearPersona,self).form_valid(form)

class OperacionExitosa(TemplateView):
        template_name = 'persona/ok.html'


class PersonaUpdateView(UpdateView):
    model = Persona
    template_name = "persona/modif.html"
    fields = ['first_name','last_name','departamento','job','anulate']
        
    success_url = reverse_lazy("persona_app:empleados_admin")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("*************  POST  ***************")
        print("====================================")
        print(request.POST['last_name'])
        print(request.POST['first_name'])
        # request.POST['first_name']='Pedro'
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        print("*************  form_valid  ***************")
        return super().form_valid(form)    



class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = "persona/borrar.html"
    context_object_name = 'lista'

    success_url = reverse_lazy("persona_app:empleados_admin")

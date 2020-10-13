from django.contrib import admin

# Register your models here.

from .models import Persona
from .models import Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'nombre_completo',
        'id',
    )
    # este es un campo que no está en la base de datos, como una especie de columna calculada
    # def full_name(sefl,obj):
    #     print(obj)
    #     return obj.last_name + ' ' + obj.first_name
    #
    search_fields = ('first_name','last_name',)
    list_filter = ('job','habilidades',)
    filter_horizontal = ('habilidades',)

admin.site.register(Persona,EmpleadoAdmin)

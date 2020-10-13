from django.contrib import admin

# Register your models here.

from .models import Tercero
from applications.departamento.models import Departamento

# Register your models here.

class TerceroAdmin(admin.ModelAdmin):
    list_display = (
        'razon_social',
        'nit',
        'departamento',
    )
    # este es un campo que no está en la base de datos, como una especie de columna calculada
    # def full_name(sefl,obj):
    #     print(obj)
    #     return obj.last_name + ' ' + obj.first_name
    #
    search_fields = ('razon_social','nit',)

admin.site.register(Tercero,TerceroAdmin)

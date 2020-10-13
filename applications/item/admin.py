from django.contrib import admin

# Register your models here.
from .models import Item, Bodegas

admin.site.register(Bodegas)


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'descripcion',
        'grupo',
    )
    # este es un campo que no está en la base de datos, como una especie de columna calculada
    def full_name(sefl,obj):
        # print(obj)
        return obj.codigo + ' ' + obj.descripcion
    #
    search_fields = ('codigo','descripcion',)
    # list_filter = ('grupo','bodega',)
    filter_horizontal = ('bodegas',)

admin.site.register(Item,ItemAdmin)

from django.shortcuts import render

from django.views.generic import (
        TemplateView, 
        ListView, 
        CreateView
)

from .models import Item

# Create your views here.


class ListarItem(ListView):
    template_name = "item/items.html"
    model = Item
    context_object_name = 'lista'
    paginate_by = 4
    ordering = 'descripcion'


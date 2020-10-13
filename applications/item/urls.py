from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('item/',views.ListarItem.as_view()),
]

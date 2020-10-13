from django.db import models
from applications.departamento.models import Departamento

# Create your models here.

class Tercero(models.Model):
    razon_social = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    maximo_descuento = models.IntegerField()
    correo = models.EmailField(blank=True)
    sitio_web = models.URLField(null=True)
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now=True)
    anulado = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.razon_social} - {self.nit}'
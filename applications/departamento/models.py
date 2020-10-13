from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre',max_length=100, unique=True)
    shor_name = models.CharField('Nombre corto',max_length=50, blank=True)
    anulate = models.BooleanField('Anulado',default=False)

    class Meta:
        verbose_name = 'Mi departamento' #este para cuando es el título sobre el grid
        verbose_name_plural = 'Areas de la empresa' #este es el título de la primera página
        ordering = ['name']
        unique_together = ('name','shor_name')

    def __str__(self):
        anu=''
        if self.anulate == True:
            anu=' (Anulado)'

        return f'{self.id} - {self.name} {self.shor_name} {anu}'
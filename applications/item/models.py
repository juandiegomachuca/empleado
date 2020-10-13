from django.db import models


# Create your models here.
class Bodegas(models.Model):
    bodega = models.CharField('Bodega', max_length=50)
       
    class Meta:
        verbose_name = 'Bodega' #este para cuando es el título sobre el grid
        verbose_name_plural = 'Bodegas' #este es el título de la primera página
 
    def __str__(self):
        return f'{self.id} - {self.bodega}'



class Item(models.Model):
    GRUPOS = [
                (1,'Medicamentos'),
                (2,'Droga blanca'),
                (3,'Perfumes'),
                (4,'Accesorios')
            ]

    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    grupo = models.IntegerField('Grupo', choices=GRUPOS, default=1)
    cantidad = models.IntegerField()
    precio = models.IntegerField(default=0)
    bodegas = models.ManyToManyField(Bodegas)


    class Meta:
        verbose_name = 'Item' #este para cuando es el título sobre el grid
        verbose_name_plural = 'Items' #este es el título de la primera página
        ordering = ['codigo']

    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'
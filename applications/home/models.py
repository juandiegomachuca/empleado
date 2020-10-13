from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    valor = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.titulo} - {self.subtitulo}, {self.cantidad}'
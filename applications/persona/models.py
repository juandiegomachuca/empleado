from django.db import models

from ckeditor.fields import RichTextField

from applications.departamento.models import Departamento

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=200)
       
    class Meta:
        verbose_name = 'Habilidad' #este para cuando es el título sobre el grid
        verbose_name_plural = 'Habilidades' #este es el título de la primera página
 
    def __str__(self):
        return f'{self.id} - {self.habilidad}'


class Persona(models.Model):
    PROFESIONES = [('ING','Ingeniero'),
                        ('CON','Contador'),
                        ('VEN','Vendedor'),
                        ('OBR','Obrero'),
                        ('PRG','Programador'),
                        ('ADM','Administrador')
                        ]

    first_name = models.CharField('Nombre',max_length=100, unique=False)
    last_name = models.CharField('Apellido',max_length=50, blank=True)
    nombre_completo = models.CharField('Nombre completo',max_length=150, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    job = models.CharField('Profesión', max_length=3, choices=PROFESIONES)
    avatar = models.ImageField('Foto', 
                                upload_to='empleado', 
                                height_field=None, 
                                width_field=None, 
                                max_length=120, 
                                null=True,
                                blank=True
                                )
    anulate = models.BooleanField('Anulado',default=False)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField(blank=True)

    class Meta:
        verbose_name = 'Empleado' #este para cuando es el título sobre el grid
        verbose_name_plural = 'Empleados' #este es el título de la primera página
        ordering = ['first_name']
        # unique_together = ('name','shor_name')

    def __str__(self):
        anu=''
        if self.anulate == True:
            anu=' (Anulado)'

        return f'{self.id} - {self.first_name} {self.last_name} {anu}'
# Generated by Django 3.1.1 on 2020-10-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_persona_hoja_vida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]

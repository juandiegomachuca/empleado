# Generated by Django 3.1.1 on 2020-10-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_auto_20201004_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='nombre_completo',
            field=models.CharField(blank=True, max_length=150, verbose_name='Nombre completo'),
        ),
    ]

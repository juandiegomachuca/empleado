# Generated by Django 3.1.1 on 2020-10-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=200, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['first_name'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterField(
            model_name='persona',
            name='job',
            field=models.CharField(choices=[('ING', 'Ingeniero'), ('CON', 'Contador'), ('VEN', 'Vendedor'), ('OBR', 'Obrero'), ('PRG', 'Programador'), ('ADM', 'Administrador')], max_length=3, verbose_name='Profesión'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodegas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodega', models.CharField(max_length=50, verbose_name='Bodega')),
            ],
            options={
                'verbose_name': 'Bodega',
                'verbose_name_plural': 'Bodegas',
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
    ]

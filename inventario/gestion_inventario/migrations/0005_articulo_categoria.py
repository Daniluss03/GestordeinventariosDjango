# Generated by Django 5.0.6 on 2024-07-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inventario', '0004_articulo_fecha_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.CharField(choices=[('Gaseosas', 'gaseosas'), ('ropa', 'Ropa'), ('hogar', 'Hogar'), ('alimentos', 'Alimentos'), ('otros', 'Otros')], default='Gaseosas', max_length=100),
        ),
    ]

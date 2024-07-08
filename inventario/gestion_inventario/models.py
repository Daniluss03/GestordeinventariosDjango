from django.db import models
from django.utils import timezone

class Articulo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ventas = models.IntegerField(default=0)  # Campo para registrar las ventas
    entradas = models.IntegerField(default=0)  # Campo para registrar las entradas
    fecha_registro = models.DateField(default=timezone.now)  # Campo para la fecha de registro

    CATEGORIAS = [
        ('Gaseosas', 'gaseosas'),
        ('ropa', 'Ropa'),
        ('hogar', 'Hogar'),
        ('alimentos', 'Alimentos'),
        ('otros', 'Otros'),
    ]
    
    categoria = models.CharField(max_length=100, choices=CATEGORIAS,default='Gaseosas')  # Campo para la categoría del artículo

    def __str__(self):
        return self.nombre

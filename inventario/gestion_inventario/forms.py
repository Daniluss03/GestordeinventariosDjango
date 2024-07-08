# gestion_inventario/forms.py

from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'descripcion', 'cantidad', 'precio', 'entradas', 'ventas','fecha_registro','categoria']

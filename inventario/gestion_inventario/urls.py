# gestion_inventario/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generar_pdf_articulos/', views.generar_pdf_articulos, name='generar_pdf_articulos'),
    path('articulos/', views.listar_articulos, name='listar_articulos'),
    path('agregar/', views.agregar_articulo, name='agregar_articulo'),
    path('actualizar/<int:pk>/', views.actualizar_articulo, name='actualizar_articulo'),
     # Otras rutas aquí...
    path('descargar-excel/', views.descargar_excel_articulos, name='descargar_excel_articulos'),
    path('eliminar/<int:pk>/', views.eliminar_articulo, name='eliminar_articulo'),
]

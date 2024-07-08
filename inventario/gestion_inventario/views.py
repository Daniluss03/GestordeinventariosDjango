# gestion_inventario/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from .forms import ArticuloForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from django.shortcuts import render
from .models import Articulo
# views.py
from django.http import HttpResponse
from .utils import generar_excel_articulos


from .utils import (generar_grafica_productos_mas_vendidos_por_categoria,
                    generar_grafica_productos_menos_vendidos_por_categoria,
                    generar_grafica_productos_mas_entradas_por_categoria,
                    generar_grafica_productos_menos_entradas_por_categoria)
def listar_articulos(request):
  
      # Obtener todos los artículos agrupados por categoría
    categorias = Articulo.objects.values_list('categoria', flat=True).distinct()
    articulos_por_categoria = {}
    # Generar la gráfica de productos más vendidos
    generar_grafica_productos_mas_vendidos_por_categoria()
    generar_grafica_productos_menos_vendidos_por_categoria()
    generar_grafica_productos_mas_entradas_por_categoria()
    generar_grafica_productos_menos_entradas_por_categoria()

    for categoria in categorias:
        articulos_por_categoria[categoria] = Articulo.objects.filter(categoria=categoria)

    # Renderizar la plantilla y pasar los datos necesarios
    return render(request, 'gestion_inventario/listar_articulos.html', {'articulos_por_categoria': articulos_por_categoria})

def agregar_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'gestion_inventario/agregar_articulo.html', {'form': form})

def actualizar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'gestion_inventario/agregar_articulo.html', {'form': form})

def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('listar_articulos')
    return render(request, 'gestion_inventario/eliminar_articulo.html', {'articulo': articulo})

def index(request):
    return render(request, 'gestion_inventario/index.html')

def generar_pdf_articulos(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="articulos.pdf"'

    # Crear el documento PDF
    p = canvas.Canvas(response)
    p.drawString(100, 800, "Listado de Artículos")

    # Obtener los datos de los artículos desde la base de datos
    articulos = Articulo.objects.all()

    # Escribir los datos en el PDF
    y = 750
    for articulo in articulos:
        p.drawString(100, y, f"Nombre: {articulo.nombre}")
        p.drawString(100, y - 20, f"Ventas: {articulo.ventas}")
        p.drawString(100, y - 40, f"Entradas: {articulo.entradas}")
        y -= 60

    p.showPage()
    p.save()

    return response

def vender_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.ventas += 1
    articulo.save()
    return redirect('listar_articulos')

def ingresar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    articulo.entradas += 1
    articulo.save()
    return redirect('listar_articulos')


def descargar_excel_articulos(request):
    # Generar el archivo Excel
    excel_path = generar_excel_articulos()

    # Abre el archivo y devuelve su contenido como una respuesta HTTP
    with open(excel_path, 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=articulos.xlsx'
        return response

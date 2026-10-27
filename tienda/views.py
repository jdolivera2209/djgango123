from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto


def mostrar_productos(request):

    productos = Producto.objects.all()

    nombres = []

    for p in productos:
        nombres.append(p.nombre)

    return HttpResponse("<br>".join(nombres))


def mostrar_productos2(request):

    productos = Producto.objects.all()

    return render(
        request,
        'productos.html',
        {'productos': productos}
    )
def actualizar_producto(request):

    producto = Producto.objects.get(id=1)

    producto.precio = 5000

    producto.save()

    return HttpResponse("Producto actualizado")
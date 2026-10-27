from django.http import HttpResponse
from django.shortcuts import render
from .models import Competidor


def inicio(request):
    return HttpResponse("Bienvenido a Senasoft")


def registro(request):

    if request.method == "POST":

        Competidor.objects.create(
            nombre=request.POST.get("nombre"),
            centro=request.POST.get("centro"),
            categoria=request.POST.get("categoria")
        )

        return HttpResponse(
            "Competidor registrado"
        )

    return render(
        request,
        "registro.html"
    )
def competidores(request):

    lista = Competidor.objects.all()

    return render(
        request,
        "competidores.html",
        {"competidores": lista}
    )
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pelicula


def registrar_pelicula(request):

    if request.method == "POST":

        titulo = request.POST.get("titulo")

        imagen = request.FILES.get("imagen")

        Pelicula.objects.create(
            titulo=titulo,
            imagen=imagen
        )

        return HttpResponse(
            "Pelicula guardada"
        )

    return render(
        request,
        "peliculas.html"
    )
def listar_peliculas(request):

    peliculas = Pelicula.objects.all()

    return render(
        request,
        "lista_peliculas.html",
        {
            "peliculas": peliculas
        }
    )
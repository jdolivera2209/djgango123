from django.urls import path
from . import views

urlpatterns = [

    path(
        'registro/',
        views.registrar_pelicula
    ),

    path(
        'lista/',
        views.listar_peliculas
    ),
]
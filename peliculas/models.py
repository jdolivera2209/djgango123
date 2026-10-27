from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='peliculas/')

    def __str__(self):
        return self.titulo
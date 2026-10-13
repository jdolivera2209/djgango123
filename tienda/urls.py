from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.mostrar_productos),
    path('productos2/', views.mostrar_productos2),
]
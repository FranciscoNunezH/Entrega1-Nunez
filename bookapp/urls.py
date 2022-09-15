from django.urls import path
from bookapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('libros_formulario/', libros_formulario, name='libros_formulario'),
    path('busquedaLibro/', busquedaLibro, name='busquedaLibro'),
    path('buscar/', buscar, name='buscar'),
    path('user/', user, name='user'),
    path('author/', author, name='author'),
]

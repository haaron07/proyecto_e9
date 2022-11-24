from django.urls import path
from .views import index,peliculas,series,videogames,pelis,pelis_crear,pelis_editar,pelis_eliminar,peli_data
from .views import serie,serie_crear,serie_data,serie_eliminar,serie_editar
from .views import vg,vg_crear,vg_data,vg_editar,vg_eliminar
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', index,name="index"),
    ##URLS DE PROYECTO PELICULA##
    path('peliculas',peliculas,name="peliculas"),
    path('pelis-index',pelis,name="pelis"),
    path('pelis-crear',pelis_crear,name="pelis_crear"),
    path('pelis-editar/<int:id>',pelis_editar,name="pelis_editar"),
    path('pelis-details/<int:id>',peli_data,name="pelis_details"),
    path('pelis-eliminar/<int:id>',pelis_eliminar,name="pelis_eliminar"),
    ##URLS DE PROYECTO SERIES##
    path('series',series,name="series"),
    path('serie-index',serie,name="serie"),
    path('serie-crear',serie_crear,name="series_crear"),
    path('serie-editar/<int:id>',serie_editar,name="series_editar"),
    path('serie-details/<int:id>',serie_data,name="series_details"),
    path('serie-eliminar/<int:id>',serie_eliminar,name="series_eliminar"),
    ##URLS DE PROYECTO VIDEOJUEGOS##
    path('videogames',videogames,name="videogames"),
    path('vg-index',vg,name="vg"),
    path('vg-crear',vg_crear,name="vg_crear"),
    path('vg-editar/<int:id>',vg_editar,name="vg_editar"),
    path('vg-details/<int:id>',vg_data,name="vg_details"),
    path('vg-eliminar/<int:id>',vg_eliminar,name="vg_eliminar"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
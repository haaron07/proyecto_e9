from django.shortcuts import render,redirect
from .models import Movies,Series,VideoGames
from .forms import MovieForm,SerieForm,GameForm
# Create your views here.

def index(request):
    return render(request,'index.html')

def peliculas(request):
    pelis=Movies.objects.all()
    return render(request,'pelis.html',{'data':pelis})

def series(request):
    pelis=Series.objects.all()
    return render(request,'series.html',{'data':pelis})

def videogames(request):
    pelis=VideoGames.objects.all()
    return render(request,'videogames.html',{'data':pelis})


##CRUD DE PELICULAS##
def pelis(request):
    data={
        'pelis': Movies.objects.all()
    }
    return render(request,'pelis/index.html',data)

def peli_data(request,id):
    company = Movies.objects.get(id = id)
    return render(request,'pelis/details.html', {'detalle': company})

def pelis_crear(request):
    formulario = MovieForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pelis')
    return render(request, 'pelis/crear.html', {'formulario': formulario})

def pelis_editar(request, id):
    company = Movies.objects.get(id = id)
    formulario = MovieForm(request.POST or None, instance=company)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('pelis')
    return render(request,'pelis/editar.html', {'formulario': formulario})

def pelis_eliminar(request, id):
    company = Movies.objects.get(id=id)
    company.delete()
    return redirect('pelis')

##CRUD DE SERIES##
def serie(request):
    data={
        'pelis': Series.objects.all()
    }
    return render(request,'series/index.html',data)

def serie_data(request,id):
    company = Series.objects.get(id = id)
    return render(request,'series/details.html', {'detalle': company})

def serie_crear(request):
    formulario = SerieForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('serie')
    return render(request, 'series/crear.html', {'formulario': formulario})

def serie_editar(request, id):
    company = Series.objects.get(id = id)
    formulario = SerieForm(request.POST or None, instance=company)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('serie')
    return render(request,'series/editar.html', {'formulario': formulario})

def serie_eliminar(request, id):
    company = Series.objects.get(id=id)
    company.delete()
    return redirect('serie')

##CRUD DE VIDEJUEGOS##
def vg(request):
    data={
        'pelis': VideoGames.objects.all()
    }
    return render(request,'videogames/index.html',data)

def vg_data(request,id):
    company = VideoGames.objects.get(id = id)
    return render(request,'videogames/details.html', {'detalle': company})

def vg_crear(request):
    formulario = GameForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('vg')
    return render(request, 'videogames/crear.html', {'formulario': formulario})

def vg_editar(request, id):
    company = VideoGames.objects.get(id = id)
    formulario = GameForm(request.POST or None, instance=company)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('vg')
    return render(request,'videogames/editar.html', {'formulario': formulario})

def vg_eliminar(request, id):
    company = VideoGames.objects.get(id=id)
    company.delete()
    return redirect('vg')
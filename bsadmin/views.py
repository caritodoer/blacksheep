from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import *

# Create your views here.

def l_veterinario(request):
	queryset = Veterinario.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado Veterinario"
	}
	return render(request, "lista_vet.html", context)

def l_categoria(request):
	queryset = Categoria.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Categorias de Establecimientos"
	}
	return render(request, "lista_aux.html", context)

def l_explotacion(request):
	queryset = Explotacion.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Explotaciones de Establecimientos"
	}
	return render(request, "lista_aux.html", context)

def l_especie(request):
	queryset = Especie.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Especies"
	}
	return render(request, "lista_aux.html", context)


def l_muestra(request):
	queryset = Muestra.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Muestras"
	}
	return render(request, "lista_aux.html", context)

def l_establecimiento(request):
	queryset = Establecimiento.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Establecimientos"
	}
	return render(request, "lista_establecimiento.html", context)

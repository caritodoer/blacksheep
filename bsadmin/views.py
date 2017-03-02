from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *

# Veterinario

def l_veterinario(request):
	queryset = Veterinario.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado Veterinario"
	}
	return render(request, "lista_vet.html", context)

# Categoria - Carito

def l_categoria(request):
	queryset = Categoria.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Categorias de Establecimientos"
	}
	return render(request, "lista_aux.html", context)

def a_categoria(request):
	form = CategoriaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : "Nueva Categoria",
		"form" : form,
	}
	return render(request, "alta_aux.html", context)

def v_categoria(request, id=None):
	instance = get_object_or_404(Categoria, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Categoria",
	}
	return render(request, "detalle.html", context)

def u_categoria(request, id=None):
	instance = get_object_or_404(Categoria,id=id)
	form = CategoriaForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : "Modificar Categoria",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_aux.html", context)

def d_categoria(request, id=None):
	instance = get_object_or_404(Categoria, id=id)
	instance.delete()
	return redirect("bsadmin:l_categoria")


#Explotacion

def l_explotacion(request):
	queryset = Explotacion.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Explotaciones de Establecimientos"
	}
	return render(request, "lista_aux.html", context)

# Especie

def l_especie(request):
	queryset = Especie.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Especies"
	}
	return render(request, "lista_aux.html", context)

def a_especie(request):
	form = EspecieForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : "Nueva Especie",
		"form" : form,
	}
	return render(request, "alta_aux.html", context)

def v_especie(request, id=None):
	instance = get_object_or_404(Especie, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Especie",
	}
	return render(request, "detalle.html", context)

def u_especie(request, id=None):
	instance = get_object_or_404(Especie,id=id)
	form = EspecieForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : "Modificar Especie",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_aux.html", context)

def d_especie(request, id=None):
	instance = get_object_or_404(Especie, id=id)
	instance.delete()
	return redirect("bsadmin:l_especie")


# Muestra

def l_muestra(request):
	queryset = Muestra.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Muestras"
	}
	return render(request, "lista_aux.html", context)

def a_muestra(request):
	form = MuestraForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : "Nueva Muestra",
		"form" : form,
	}
	return render(request, "alta_aux.html", context)

def v_muestra(request, id=None):
	instance = get_object_or_404(Muestra, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Muestra",
	}
	return render(request, "detalle.html", context)

def u_muestra(request, id=None):
	instance = get_object_or_404(Muestra,id=id)
	form = MuestraForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : "Modificar Muestra",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_aux.html", context)

def d_muestra(request, id=None):
	instance = get_object_or_404(Muestra, id=id)
	instance.delete()
	return redirect("bsadmin:l_muestra")

# Establecimiento

def l_establecimiento(request):
	queryset = Establecimiento.objects.all()
	context = {
		"object_list": queryset,
		"title": "Listado de Establecimientos"
	}
	return render(request, "lista_establecimiento.html", context)

# Especializacion

def l_especializacion(request):
	queryset = Especializacion.objects.all()
	context = {
		"object_list" : queryset,
		"title" : "Listado de Especializaciones",
	}
	return render(request, "lista_aux.html", context)

def a_especializacion(request):
	form = EspecializacionForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : "Nueva Especializacion",
		"form" : form,
	}
	return render(request, "alta_aux.html", context)

def v_especializacion(request, id=None):
	instance = get_object_or_404(Especializacion, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Especializacion",
	}
	return render(request, "detalle.html", context)

def u_especializacion(request, id=None):
	instance = get_object_or_404(Especializacion,id=id)
	form = EspecializacionForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title" : "Modificar Especializacion",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_aux.html", context)

def d_especializacion(request, id=None):
	instance = get_object_or_404(Especializacion, id=id)
	instance.delete()
	return redirect("bsadmin:l_especializacion")


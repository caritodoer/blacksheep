from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from .models import *
from .forms import *
from django.core import serializers

def home_admin(request):
	return render(request, "home_admin.html")

#Alta diagnostico

def diagnosticoAjax(request):
	if request.method == 'POST':
		descripcion = request.POST['descripcion'] 
		tecnica = request.POST['tecnica']
		posMuestra = request.POST['muestra']
		muestra = get_object_or_404(Muestra,id=posMuestra)
		
		tercerizacion = request.POST['tercerizacion']
		if tercerizacion == "true":
			tercerizacion = True
		else:
			tercerizacion = False
			
		piepagina = request.POST['piepagina']
			
		Diagnostico.objects.create(
			descripcion = descripcion,
			tecnica = tecnica,
			muestra = muestra,
			tercerizacion = tercerizacion,
			piepagina = piepagina,
    	)

		return HttpResponse('')

# Categoria

def j_categoria(request):
	queryset = Categoria.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_categoriaid(request,id=None):
	queryset = Categoria.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_categoria(request):
	queryset = Categoria.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Categorias de Establecimientos"
	}
	return render(request, "lista_aux.html", context)

def a_categoria(request):
	# si no estoy logueada no me deberia aparecer la pagina
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	form = CategoriaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
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
	else:
		print (form.errors)
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


##explotacion
def j_explotacion(request):
	queryset = Explotacion.objects.all().values().order_by('id')   
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_explotacionid(request,id=None):
	queryset = Explotacion.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_explotacion(request):
	queryset = Explotacion.objects.all().order_by('id')
	context = {
		"object_list":queryset,
		"title":"Listado de Explotacion"
	}
	return render(request,"lista_aux.html",context)

def a_explotacion(request):
	form = ExplotacionForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit='False')
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Crear Explotacion",
		"form": form
		}
	return render(request,"alta_aux.html",context)

def v_explotacion(request, id=None):
	instance = get_object_or_404(Explotacion, id=id)
	context = {
		"instance":instance,
		"title": "Detalle de explotacion"
	} 
	return render(request,"detalle.html",context)

def u_explotacion(request,id=None):
	instance = get_object_or_404(Explotacion, id=id)
	form = ExplotacionForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context={
		"title":"Modificar Explotacion",
		"instance":instance,
		"form":form
	}
	return render(request,"alta_aux.html",context)

def d_explotacion(request,id=None):
	instance=get_object_or_404(Explotacion, id=id)
	instance.delete()
	return redirect("bsadmin:l_explotacion")

# # Especie
# def j_especie(request):
# 	queryset = Especie.objects.all()
# 	queryset = serializers.serialize('json',queryset)
# 	return HttpResponse(queryset,content_type='application/json')

def j_especie(request):
    queryset = Especie.objects.all().values().order_by('id')  # or simply .values() to get all fields
    queryset = list(queryset)  # important: convert the QuerySet to a list object
    return JsonResponse(queryset, safe=False)

def j_especieid(request,id=None):
	queryset = Especie.objects.filter(id=id).values()  # or simply .values() to get all fields
	queryset = list(queryset)  # important: convert the QuerySet to a list object
	return JsonResponse(queryset, safe=False)

def l_especie(request):
	queryset = Especie.objects.all().order_by('id')
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
	else:
		print (form.errors)
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
	else:
		print (form.errors)
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
def j_muestra(request):
	queryset = Muestra.objects.all().values().order_by('id')    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_muestraid(request,id=None):
	queryset = Muestra.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_muestra(request):
	queryset = Muestra.objects.all().order_by('id')
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
	else:
		print (form.errors)
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
	else:
		print (form.errors)
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

# Especializacion
def j_especializacion(request):
	queryset = Especializacion.objects.all().values().order_by('id')    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_especializacionid(request,id=None):
	queryset = Especializacion.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_especializacion(request):
	queryset = Especializacion.objects.all().order_by('id')
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
	else:
		print (form.errors)
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
	else:
		print (form.errors)
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

# motivos

def j_motivos(request):
	queryset = Motivos.objects.all().values().order_by('id')    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_motivosid(request,id=None):
	queryset = Motivos.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def a_motivos(request):
	form = MotivosForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Nuevo Motivos",
		"form": form,
	}

	return render(request, "alta_aux.html", context)

def v_motivos(request, id=None):
	instance = get_object_or_404(Motivos, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de Motivos"
	}	
	return render(request, "detalle.html", context)

def l_motivos(request):
	queryset = Motivos.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado Motivos"
	}
	return render(request, "lista_aux.html", context)


def u_motivos(request, id=None):
	instance = get_object_or_404(Motivos, id=id)
	form = MotivosForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Modificar especializacion",
		"instance": instance,
		"form": form
	}
	return render(request, "alta_aux.html", conext)

def d_motivos(request, id=None):
	instance = get_object_or_404(Motivos, id=id)
	instance.delete()
	return redirect("bsadmin:l_motivos")

#categoriaE

def j_categoriae(request):
	queryset = CategoriaE.objects.all().values().order_by('id')    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_categoriaeid(request,id=None):
	queryset = CategoriaE.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def a_categoriae(request):
	form = CategoriaEForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Nuevo Categoria E",
		"form": form,
	}
	return render(request, "alta_aux2.html", context)

def v_categoriae(request, id=None):
	instance = get_object_or_404(CategoriaE, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de Categoria"
	}	
	return render(request, "detalle2.html", context)

def l_categoriae(request):
	queryset = CategoriaE.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado Categoria"
	}
	return render(request, "lista_aux2.html", context)

def u_categoriae(request, id=None):	
	instance = get_object_or_404(CategoriaE, id=id)
	form = CategoriaEForm(request.POST or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Modificar Categoria",
		"instance": instance,
		"form": form
	}
	return render(request, "alta_aux2.html", context)

def d_categoriae(request, id=None):
	instance = get_object_or_404(CategoriaE, id=id)
	instance.delete()
	return redirect("bsadmin:l_categoriae")


# Raza

def j_raza(request):
	queryset = Raza.objects.all().values().order_by('id')    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_razaid(request,id=None):
	queryset = Raza.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_raza(request):
	queryset = Raza.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Razas"
	}
	return render(request, "lista_aux2.html", context)

def a_raza(request):
	form = RazaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Nueva Raza",
		"form": form,
	}

	return render(request, "alta_aux2.html", context)

def v_raza(request, id=None):
	instance = get_object_or_404(Raza, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de Raza"
	}	
	return render(request, "detalle2.html", context)

def l_raza(request):
	queryset = Raza.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado Raza"
	}
	return render(request,"lista_aux2.html",context)	


def u_raza(request, id=None):
	instance = get_object_or_404(Raza, id=id)
	form = RazaForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Modificar Raza",
		"instance": instance,
		"form": form
	}
	return render(request, "alta_aux2.html", context)

def d_raza(request, id=None):
	instance = get_object_or_404(Raza, id=id)
	instance.delete()
	return redirect("bsadmin:l_raza")


#parametros

def j_parametros(request):
	queryset = Parametros.objects.all().values().order_by('id')    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)
	
def j_parametrosid(request,id=None):
	queryset = Parametros.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_parametros(request):
	queryset = Parametros.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Parametros"
	}
	return render(request, "lista_parametros.html", context)

def a_parametros(request):
	form = ParametrosForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Nuevo Parametro",
		"form": form,
	}
	return render(request, "alta_parametros.html", context)

def v_parametros(request, id=None):
	instance = get_object_or_404(Parametros, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de Parametros"
	}	
	return render(request, "detalle_parametros.html", context)


def u_parametros(request, id=None):
	instance = get_object_or_404(Parametros, id=id)
	form = ParametrosForm(request.POST or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Modificar Parametros",
		"instance": instance,
		"form": form
	}
	return render(request, "alta_parametros.html", context)

def d_parametros(request, id=None):
	instance = get_object_or_404(Parametros, id=id)
	instance.delete()
	return redirect("bsadmin:l_parametros")

#diagnostico
def j_diagnostico(request):
	queryset = Diagnostico.objects.all().values().order_by('id')    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_diagnosticoid(request,id=None):
	queryset = Diagnostico.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)


def l_diagnostico(request):
	queryset = Diagnostico.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Diagnostico"
	}
	return render(request, "lista_diagnostico.html", context)

def a_diagnostico(request):
	form = DiagnosticoForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Nuevo Diagnostico",
		"form": form,
	}
	return render(request, "alta_diagnostico.html", context)

def v_diagnostico(request, id=None):
	instance = get_object_or_404(Diagnostico, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de Diagnostico"
	}	
	return render(request, "detalle_diagnostico.html", context)


def u_diagnostico(request, id=None):
	instance = get_object_or_404(Diagnostico, id=id)
	form = DiagnosticoForm(request.POST or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Modificar Diagnostico",
		"instance": instance,
		"form": form
	}
	return render(request, "alta_diagnostico.html", context)

def d_diagnostico(request, id=None):
	instance = get_object_or_404(Diagnostico, id=id)
	instance.delete()
	return redirect("bsadmin:l_diagnostico")

#valoresreferencia
def j_valoresreferencia(request):
	queryset = ValoresReferencia.objects.all().values().order_by('id')    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_valoresreferenciaid(request,id=None):
	queryset = ValoresReferencia.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_valoresreferencia(request):
	queryset = ValoresReferencia.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de ValoresReferencia"
	}
	return render(request, "lista_valoresreferencia.html", context)

def a_valoresreferencia(request):
	form = ValoresReferenciaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Nueva ValoresReferencia",
		"form": form,
	}
	return render(request, "alta_valoresreferencia.html", context)

def v_valoresreferencia(request, id=None):
	instance = get_object_or_404(ValoresReferencia, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de ValoresReferencia"
	}	
	return render(request, "detalle_valoresreferencia.html", context)


def u_valoresreferencia(request, id=None):
	instance = get_object_or_404(ValoresReferencia, id=id)
	form = ValoresReferenciaForm(request.POST or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Modificar Valores Referencia",
		"instance": instance,
		"form": form
	}
	return render(request, "alta_valoresreferencia.html", context)

def d_valoresreferencia(request, id=None):
	instance = get_object_or_404(ValoresReferencia, id=id)
	instance.delete()
	return redirect("bsadmin:l_valoresreferencia")


#veterinario
def j_veterinario(request):
	queryset = Veterinario.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_veterinarioid(request,id=None):
	queryset = Veterinario.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_veterinario(request):
	queryset = Veterinario.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de veterinario"
	}
	return render(request, "lista_veterinario.html", context)

def a_veterinario(request):
	form = VeterinarioForm(request.POST or None)
	if form.is_valid():

		instance = form
		instance.save()
		# MANY TO MANY
		for x in request.POST.getlist('form.especializaciones'): #form.especializaciones es el que esta dentro del VeterinarioForm
			instance.Especializacion.add(x) # Este trae la info desde la taba Especializacion
		instance = form.save(commit=False) # Guarda el M2M
		
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)

	context = {
		"title": "Nuevo veterinario",
		"form": form,
	}
	return render(request, "alta_veterinario.html", context)

def v_veterinario(request, id=None):
	instance = get_object_or_404(Veterinario, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de veterinario"
	}	
	return render(request, "detalle_veterinario.html", context)


def u_veterinario(request, id=None):
	instance = get_object_or_404(Veterinario, id=id)
	form = VeterinarioForm(request.POST or None, instance=instance)

	if form.is_valid():

		instance = form
		instance.save()

		for x in request.POST.getlist('form.especializaciones'):
			instance.Especializacion.add(x)
		instance = form.save(commit=False)
		
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Modificar veterinario",
		"instance": instance,
		"form": form
	}
	return render(request, "alta_veterinario.html", context)

def d_veterinario(request, id=None):
	instance = get_object_or_404(Veterinario, id=id)
	instance.delete()
	return redirect("bsadmin:l_veterinario")

#establecimiento
def j_establecimiento(request):
	queryset = Establecimiento.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_establecimientoid(request,id=None):
	queryset = Establecimiento.objects.filter(id=id).values()
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_establecimiento(request):
	queryset = Establecimiento.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de establecimiento"
	}
	return render(request, "lista_establecimiento.html", context)

def a_establecimiento(request):
	form = EstablecimientoForm(request.POST or None)
	if form.is_valid():

		instance = form
		instance.save()
			
		for x in request.POST.getlist('form.categorias' or None):
			instance.Categoria.add(x)

		for x in request.POST.getlist('form.explotacion' or None):
			instance.Explotacion.add(x)
		
		instance = form.save(commit=False)
		return HttpResponseRedirect(instance.get_absolute_url())

	else:
		print(form.errors)

	context = {
		"title": "Nuevo establecimiento",
		"form": form,
	}
	return render(request, "alta_establecimiento.html", context)

def v_establecimiento(request, id=None):
	instance = get_object_or_404(Establecimiento, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de establecimiento"
	}	
	return render(request, "detalle_establecimiento.html", context)


def u_establecimiento(request, id=None):
	instance = get_object_or_404(Establecimiento, id=id)
	form = EstablecimientoForm(request.POST or None, instance=instance)

	if form.is_valid():

		instance = form
		instance.save()

		for x in request.POST.getlist('form.especializaciones'):
			instance.Especializacion.add(x)
		instance = form.save(commit=False)
		
		return HttpResponseRedirect(instance.get_absolute_url())

	else:
		print(form.errors)

	context = {
		"title": "Modificar establecimiento",
		"instance": instance,
		"form": form
	}
	return render(request, "alta_establecimiento.html", context)

def d_establecimiento(request, id=None):
	instance = get_object_or_404(Establecimiento, id=id)
	instance.delete()
	return redirect("bsadmin:l_establecimiento")

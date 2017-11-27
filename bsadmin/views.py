from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.conf import settings
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, get_user_model, login, logout
import json

User = get_user_model()

def home_admin(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	emp = Empresa.objects.all().order_by('id')
	context = {
		"emp": emp,
	}	
	return render(request, "home_admin.html", context)
def usuarios(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = User.objects.all()
	context = {
		
		"object_list": queryset,
		"title": "Usuarios"
	}
	return render(request, "usuarios.html", context)

#Alta diagnostico


def allinone(request):
	if request.method == 'POST':
		descripcion = request.POST['descripcion'] 
		tecnica = request.POST['tecnica']
		posMuestra = request.POST['muestra']
		muestra = get_object_or_404(Muestra,id=posMuestra)
		piepagina = request.POST['piepagina']
				
		tercerizacion = request.POST['tercerizacion']
		if tercerizacion == "true":
			tercerizacion = True
		else:
			tercerizacion = False

		dicval = request.POST['dicval']
		listgroup = request.POST['listgroup']
		listtable = request.POST['listtable']
		listdesc = request.POST['listdesc']
		listdato = request.POST['listdato']
		listmed = request.POST['listmed']

		Diagnostico.objects.create(
			descripcion = descripcion,
			tecnica = tecnica,
			muestra = muestra,
			tercerizacion = tercerizacion,
			piepagina = piepagina,
		)
		diagnostico = Diagnostico.objects.latest('id')
		posdiag =  str(diagnostico.id)
		if tercerizacion == True:
			Parametros.objects.create(
			diagnostico = diagnostico,
			descripcion = "Tercearizado",
			tipo_de_dato = "S",
			unidadmedida = "",
			grupo = "Tercearizado",
			visualizacion1 = "T",
			)	
		else:

			dicval = json.loads(dicval)
			listtable = json.loads(listtable)
			listdesc = json.loads(listdesc)
			listdato = json.loads(listdato)
			listmed = json.loads(listmed)
			listgroup = json.loads(listgroup)
			
			esplist = []
			reflist = []
			deflist = []

			for z in range(len(listtable)):
				Parametros.objects.create(
				diagnostico = diagnostico,
				descripcion = listdesc[z],
				tipo_de_dato = listdato[z],
				unidadmedida = listmed[z],
				grupo = listgroup[z],
				visualizacion1 = listtable[z],
				)	

				posParametros = Parametros.objects.latest('id')
				pos = str(z)
				for k in dicval:
					if k == pos:
						for v in (dicval[pos]['listesp']):
							esplist.append(v)	
						for v in (dicval[pos]['listref']):
							reflist.append(v)
						for v in (dicval[pos]['listdef']):
							deflist.append(v)
						
						for b in range(len(esplist)):
							zespecie = get_object_or_404(Especie,id=esplist[b])
		
							ValoresReferencia.objects.create(
								especie = zespecie,
								parametros = posParametros,
								valorRef = reflist[b],
								valorDef = deflist[b],
							)		
						esplist = []
						reflist = []
						deflist = []
		html = "http://127.0.0.1:8000/diagnostico/" + posdiag + "/"
		return HttpResponse(html)



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

		data = Diagnostico.objects.latest('id')
		data = data.id
		return HttpResponse(data)

# Alta Parametros
def parametrosAjax(request):
	if request.method == 'POST':
		posDiagnostico = request.POST['diagnostico']
		diagnostico = get_object_or_404(Diagnostico,id=posDiagnostico)
		
		descripcion = request.POST['descripcion']
		tipo_de_dato = request.POST['tipo_de_dato']
		unidadmedida = request.POST['unidadmedida']
		grupo = request.POST['grupo']
		visualizacion1 = request.POST['visualizacion1']
				
		Parametros.objects.create(
			diagnostico = diagnostico,
			descripcion = descripcion,
			tipo_de_dato = tipo_de_dato,
			unidadmedida = unidadmedida,
			grupo = grupo,
			visualizacion1 = visualizacion1,
    	)

		dataPara = Parametros.objects.latest('id')
		dataPara = dataPara.id
		return HttpResponse(dataPara)
		
def valRefAjax(request):
	if request.method == 'POST':
		posEspecie = request.POST['especie']
		especie = get_object_or_404(Especie,id=posEspecie)
		
		posParametros = request.POST['parametros']
		parametros = get_object_or_404(Parametros,id=posParametros)

		valorRef = request.POST['valorRef']
		valorDef = request.POST['valorDef']
		
		
		ValoresReferencia.objects.create(
			especie = especie,
			parametros = parametros,
			valorRef = valorRef,
			valorDef = valorDef,
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Categoria.objects.all().order_by('id')
	
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(descripcion__icontains=query)

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title": "Listado de Categorias de Establecimientos"
	}
	return render(request, "lista_aux.html", context)
def a_categoria(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Categoria, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Categoria",
	}
	return render(request, "detalle.html", context)
def u_categoria(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Categoria, id=id)
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_categoria")
def activar_categoria(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Categoria, id=id)
	instance.activo = True
	instance.save()
	return redirect("bsadmin:l_categoria")

# Explotacion
def j_explotacion(request):
	queryset = Explotacion.objects.all().values().order_by('id')   
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)
def j_explotacionid(request,id=None):
	queryset = Explotacion.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)
def l_explotacion(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Explotacion.objects.all().order_by('id')
	query = request.GET.get("q")
	
	if query:
		queryset = queryset.filter(descripcion__icontains=query)

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title":"Listado de Explotacion"
	}
	return render(request,"lista_aux.html",context)
def a_explotacion(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Explotacion, id=id)
	context = {
		"instance":instance,
		"title": "Detalle de explotacion"
	} 
	return render(request,"detalle.html",context)
def u_explotacion(request,id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Explotacion, id=id)
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_explotacion")
def activar_explotacion(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Explotacion, id=id)
	instance.activo = True
	instance.save()
	return redirect("bsadmin:l_explotacion")

# Especie
def j_especie(request):
    queryset = Especie.objects.all().values().order_by('id')  # or simply .values() to get all fields
    queryset = list(queryset)  # important: convert the QuerySet to a list object
    return JsonResponse(queryset, safe=False)
def j_especieid(request,id=None):
	queryset = Especie.objects.filter(id=id).values()  # or simply .values() to get all fields
	queryset = list(queryset)  # important: convert the QuerySet to a list object
	return JsonResponse(queryset, safe=False)
def l_especie(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Especie.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(descripcion__icontains=query)

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title": "Listado de Especies"
	}
	return render(request, "lista_aux.html", context)
def a_especie(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Especie, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Especie",
	}
	return render(request, "detalle.html", context)
def u_especie(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Especie, id=id)
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_especie")
def activar_especie(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Especie, id=id)
	instance.activo = True
	instance.save()
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Muestra.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(descripcion__icontains=query)

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title": "Listado de Muestras"
	}
	return render(request, "lista_aux.html", context)
def a_muestra(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Muestra, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Muestra",
	}
	return render(request, "detalle.html", context)
def u_muestra(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Muestra, id=id)
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_muestra")
def activar_muestra(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Muestra, id=id)
	instance.activo = True
	instance.save()
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Especializacion.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(descripcion__icontains=query)

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title" : "Listado de Especializaciones",
	}
	return render(request, "lista_aux.html", context)
def a_especializacion(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Especializacion, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Especializacion",
	}
	return render(request, "detalle.html", context)
def u_especializacion(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Especializacion, id=id)
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_especializacion")
def activar_especializacion(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Especializacion, id=id)
	instance.activo = True
	instance.save()
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Motivos, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de Motivos"
	}	
	return render(request, "detalle.html", context)
def l_motivos(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Motivos.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(descripcion__icontains=query)

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title": "Listado Motivos"
	}
	return render(request, "lista_aux.html", context)
def u_motivos(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Motivos, id=id)
	form = MotivosForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title": "Modificar motivo",
		"instance": instance,
		"form": form
	}
	return render(request, "alta_aux.html", context)
def d_motivos(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Motivos, id=id)
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_motivos")
def activar_motivos(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Motivos, id=id)
	instance.activo = True
	instance.save()
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(CategoriaE, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de Categoria"
	}	
	return render(request, "detalle2.html", context)
def l_categoriae(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = CategoriaE.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(descripcion__icontains=query)|
			Q(especie__descripcion__icontains=query)
			).distinct()

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title": "Listado Categoria de Especie"
	}
	return render(request, "lista_aux2.html", context)
def u_categoriae(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404	
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(CategoriaE, id=id)
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_categoriae")
def activar_categoriae(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(CategoriaE, id=id)
	instance.activo = True
	instance.save()
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
def a_raza(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Raza, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de Raza"
	}	
	return render(request, "detalle2.html", context)
def l_raza(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Raza.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(descripcion__icontains=query)|
			Q(especie__descripcion__icontains=query)
			).distinct()

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title": "Listado de Razas"
	}
	return render(request,"lista_aux2.html",context)	
def u_raza(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Raza, id=id)
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_raza")
def activar_raza(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Raza, id=id)
	instance.activo = True
	instance.save()
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
# # VER SI SE USA l_parametros
# def l_parametros(request):
# 	queryset = Parametros.objects.all().order_by('id')
# 	context = {
# 		"object_list": queryset,
# 		"title": "Listado de Parametros"
# 	}
# 	return render(request, "lista_parametros.html", context)
# def a_parametros(request):
# 	form = ParametrosForm(request.POST or None)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		return HttpResponseRedirect(instance.get_absolute_url())
# 	else:
# 		print (form.errors)
# 	context = {
# 		"title": "Nuevo Parametro",
# 		"form": form,
# 	}
# 	return render(request, "alta_parametros.html", context)
# def v_parametros(request, id=None):
# 	instance = get_object_or_404(Parametros, id=id)
# 	context = {
# 		"instance": instance,
# 		"title": "Detalle de Parametros"
# 	}	
# 	return render(request, "detalle_parametros.html", context)
# def u_parametros(request, id=None):
# 	instance = get_object_or_404(Parametros, id=id)
# 	form = ParametrosForm(request.POST or None, instance=instance)

# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		return HttpResponseRedirect(instance.get_absolute_url())
# 	else:
# 		print (form.errors)
# 	context = {
# 		"title": "Modificar Parametros",
# 		"instance": instance,
# 		"form": form
# 	}
# 	return render(request, "alta_parametros.html", context)
# def d_parametros(request, id=None):
# 	instance = get_object_or_404(Parametros, id=id)
# 	instance.activo = False
# 	instance.save()
# 	return redirect("bsadmin:l_parametros")
# def activar_parametros(request, id=None):
# 	instance = get_object_or_404(Parametros, id=id)
# 	instance.activo = True
# 	instance.save()
# 	return redirect("bsadmin:l_parametros")

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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Diagnostico.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(descripcion__icontains=query)|
			Q(tecnica__icontains=query)|
			Q(muestra__descripcion__icontains=query)
			).distinct()

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title": "Listado de Diagnostico"
	}
	return render(request, "lista_diagnostico.html", context)
def a_diagnostico(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Diagnostico, id=id)
	diag = instance.id
	param_list = Parametros.objects.all().filter(diagnostico=diag)
	grupo_list = Parametros.objects.distinct('grupo').filter(diagnostico=diag)

	context = {
		"instance": instance,
		"param_list": param_list,
		"grupo_list": grupo_list,
		"title": "Detalle de Diagnostico"
	}	
	return render(request, "detalle_diagnostico.html", context)
# def u_diagnostico(request, id=None):
# 	if not request.user.is_authenticated() or not request.user.is_staff:
# 		raise Http404
# 	instance = get_object_or_404(Diagnostico, id=id)
# 	form = DiagnosticoForm(request.POST or None, instance=instance)

# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		return HttpResponseRedirect(instance.get_absolute_url())
# 	else:
# 		print (form.errors)
# 	context = {
# 		"title": "Modificar Diagnostico",
# 		"instance": instance,
# 		"form": form
# 	}
# 	return render(request, "alta_diagnostico.html", context)
def d_diagnostico(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Diagnostico, id=id)
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_diagnostico")
def activar_diagnostico(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Diagnostico, id=id)
	instance.activo = True
	instance.save()
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
# # VER SI SE USA l_valoresreferencia
# def l_valoresreferencia(request):
# 	queryset = ValoresReferencia.objects.all().order_by('id')
# 	context = {
# 		"object_list": queryset,
# 		"title": "Listado de ValoresReferencia"
# 	}
# 	return render(request, "lista_valoresreferencia.html", context)
# def a_valoresreferencia(request):
# 	form = ValoresReferenciaForm(request.POST or None)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		return HttpResponseRedirect(instance.get_absolute_url())
# 	else:
# 		print (form.errors)
# 	context = {
# 		"title": "Nueva ValoresReferencia",
# 		"form": form,
# 	}
# 	return render(request, "alta_valoresreferencia.html", context)
# def v_valoresreferencia(request, id=None):
# 	instance = get_object_or_404(ValoresReferencia, id=id)
# 	context = {
# 		"instance": instance,
# 		"title": "Detalle de ValoresReferencia"
# 	}	
# 	return render(request, "detalle_valoresreferencia.html", context)
# def u_valoresreferencia(request, id=None):
# 	instance = get_object_or_404(ValoresReferencia, id=id)
# 	form = ValoresReferenciaForm(request.POST or None, instance=instance)

# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		return HttpResponseRedirect(instance.get_absolute_url())
# 	else:
# 		print (form.errors)
# 	context = {
# 		"title": "Modificar Valores Referencia",
# 		"instance": instance,
# 		"form": form
# 	}
# 	return render(request, "alta_valoresreferencia.html", context)
# def d_valoresreferencia(request, id=None):
# 	instance = get_object_or_404(ValoresReferencia, id=id)
# 	instance.activo = False
# 	instance.save()
# 	return redirect("bsadmin:l_valoresreferencia")
# def activar_valoresreferencia(request, id=None):
# 	instance = get_object_or_404(ValoresReferencia, id=id)
# 	instance.activo = True
# 	instance.save()
# 	return redirect("bsadmin:l_valoresreferencia")

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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Veterinario.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(nombre__icontains=query)|
			Q(apellido__icontains=query)|
			Q(dni__icontains=query)|
			Q(especializaciones__descripcion__icontains=query)
			).distinct()

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title": "Listado de veterinario"
	}
	return render(request, "lista_veterinario.html", context)
def a_veterinario(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Veterinario, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de veterinario"
	}	
	return render(request, "detalle_veterinario.html", context)
def u_veterinario(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_veterinario")
def activar_veterinario(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Veterinario, id=id)
	instance.activo = True
	instance.save()
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	queryset = Establecimiento.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(nombre__icontains=query)|
			Q(partido__icontains=query)|
			Q(propietario__icontains=query)|
			Q(CUIT__icontains=query)|
			Q(veterinario__nombre__icontains=query)|
			Q(veterinario__apellido__icontains=query)|
			Q(categorias__descripcion__icontains=query)|
			Q(explotacion__descripcion__icontains=query)
			).distinct()

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset_list = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": queryset_list,
		"title": "Listado de establecimiento"
	}
	return render(request, "lista_establecimiento.html", context)
def a_establecimiento(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Establecimiento, id=id)
	context = {
		"instance": instance,
		"title": "Detalle de establecimiento"
	}	
	return render(request, "detalle_establecimiento.html", context)
def u_establecimiento(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
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
	instance.activo = False
	instance.save()
	return redirect("bsadmin:l_establecimiento")
def activar_establecimiento(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Establecimiento, id=id)
	instance.activo = True
	instance.save()
	return redirect("bsadmin:l_establecimiento")

# empresa

def a_empresa(request):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	if request.method == 'POST':
		form = EmpresaForm(request.POST, request.FILES)
		if form.is_valid():
			# form.save()
			instance = form.save(commit=False)
			instance.save()
			return redirect('bsadmin:home_admin')
		else:
			print (form.errors)
	else:
		form = EmpresaForm()
		print (form.errors)
	context = {
		"title" : "Cargar datos de Empresa",
		"form" : form,
	}
	return render(request, 'u_empresa.html', context)
def u_empresa(request, id=None):
	if not request.user.is_authenticated() or not request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Empresa, id=id)
	if request.method == 'POST':
		form = EmpresaForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
		else:
			print (form.errors)
	else:
		form = EmpresaForm()
		print (form.errors)
	context = {
		"title": "Modificar Empresa",
		"instance": instance,
		"form": form
	}
	return render(request, "u_empresa.html", context)

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home_user(request):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	#DetAna_queryset = DetalleAnalisisPadre.objects.all().order_by('-protocolo')
	DetAna_queryset_list = DetalleAnalisisPadre.objects.distinct('protocolo')
	
	query = request.GET.get("q")
	if query:
		DetAna_queryset_list = DetAna_queryset_list.filter(protocolo__numero__icontains=query)

	paginator = Paginator(DetAna_queryset_list, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		DetAna_queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		DetAna_queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		DetAna_queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": DetAna_queryset,
		"title": "Últimos Protocolos Registrados",
		"page_request_var": page_request_var,
	}
	return render(request, "home_user.html", context)

# Solicitud Analisis

def j_solicitudanalisis(request):
	queryset = SolicitudAnalisis.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_solicitudanalisisid(request,id=None):
	queryset = SolicitudAnalisis.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

# def l_solicitudanalisis(request):
# 	queryset = SolicitudAnalisis.objects.all().order_by('id')
# 	context = {
# 		"object_list": queryset,
# 		"title": "Listado de Solicitudes de Analisis"
# 	}
# 	return render(request, "list_solAn.html", context)

def a_solicitudanalisis(request):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	form = SolicitudAnalisisForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Nueva Solicitudes de Analisis",
		"form" : form,
	}
	return render(request, "alta_solAn.html", context)

# def v_solicitudanalisis(request, id=None):
# 	instance = get_object_or_404(SolicitudAnalisis, id=id)
# 	context = {
# 		"instance" : instance,
# 		"title": "Detalle de Solicitud de Analisis",
# 	}
# 	return render(request, "ver_solAn.html", context)

def u_solicitudanalisis(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(SolicitudAnalisis,id=id)
	form = SolicitudAnalisisForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Solicitud de Analisis",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_solAn.html", context)

def d_solicitudanalisis(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(SolicitudAnalisis, id=id)
	instance.delete()
	return redirect("bsadmin:l_solicitudanalisis")

# Protocolo

def j_protocolo(request):
	queryset = Protocolo.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_protocoloid(request,id=None):
	queryset = Protocolo.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

# def l_protocolo(request):
# 	queryset = Protocolo.objects.all().order_by('id')
# 	context = {
# 		"object_list": queryset,
# 		"title": "Listado de Protocolos"
# 	}
# 	return render(request, "list_protocolo.html", context)

def a_protocolo(request):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	form = ProtocoloForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Nuevo Protocolo",
		"form" : form,
	}
	return render(request, "alta_protocolo.html", context)

def u_protocolo(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Protocolo,id=id)
	form = ProtocoloForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Protocolo",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_protocolo.html", context)

def d_protocolo(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Protocolo, id=id)
	instance.delete()
	return redirect("bsadmin:l_protocolo")

# Individuo Padre

def j_individuopadre(request):
	queryset = IndividuoPadre.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_individuopadreid(request,id=None):
	queryset = IndividuoPadre.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

# def l_individuopadre(request):
# 	queryset = IndividuoPadre.objects.all().order_by('id')
# 	context = {
# 		"object_list": queryset,
# 		"title": "Listado de Individuos Padre"
# 	}
# 	return render(request, "list_indivp.html", context)

def a_individuopadre(request):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	form = IndividuoPadreForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Registrar Individuo/s",
		"form" : form,
	}
	return render(request, "alta_indivp.html", context)

# def v_individuopadre(request, id=None):
# 	instance = get_object_or_404(IndividuoPadre, id=id)
# 	context = {
# 		"instance" : instance,
# 		"title": "Detalle de Individuo Padre",
# 	}
# 	return render(request, "ver_indivp.html", context)

def u_individuopadre(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(IndividuoPadre,id=id)
	form = IndividuoPadreForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Individuo Padre",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_indivp.html", context)

def d_individuopadre(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(IndividuoPadre, id=id)
	instance.delete()
	return redirect("bsadmin:l_individuopadre")

# Individuos

def j_individuos(request):
	queryset = Individuos.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_individuosid(request,id=None):
	queryset = Individuos.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

# def l_individuos(request):
# 	queryset = Individuos.objects.all().order_by('id')
# 	context = {
# 		"object_list": queryset,
# 		"title": "Listado de Individuos"
# 	}
# 	return render(request, "list_indiv.html", context)

# def a_individuos(request):
# 	form = IndividuosForm(request.POST or None)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		return HttpResponseRedirect(instance.get_absolute_url())
# 	else:
# 		print (form.errors)
# 	context = {
# 		"title" : "Nuevo Individuo",
# 		"form" : form,
# 	}
# 	return render(request, "alta_indiv.html", context)

# def v_individuos(request, id=None):
# 	instance = get_object_or_404(Individuos, id=id)
# 	context = {
# 		"instance" : instance,
# 		"title": "Detalle de Individuo",
# 	}
# 	return render(request, "ver_indiv.html", context)

def u_individuos(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Individuos,id=id)
	form = IndividuosForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Individuo",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_indiv.html", context)

def d_individuos(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Individuos, id=id)
	instance.delete()
	return redirect("bsadmin:l_individuos")

# Detalle Analisis

def j_detalleanalisis(request):
	queryset = DetalleAnalisis.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_detalleanalisisid(request,id=None):
	queryset = DetalleAnalisis.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

# def l_detalleanalisis(request):
# 	queryset = DetalleAnalisis.objects.all().order_by('id')
# 	context = {
# 		"object_list": queryset,
# 		"title": "Listado de Detalle Analisis"
# 	}
# 	return render(request, "list_detAn.html", context)

# def a_detalleanalisis(request):
# 	form = DetalleAnalisisForm(request.POST or None)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		return HttpResponseRedirect(instance.get_absolute_url())
# 	else:
# 		print (form.errors)
# 	context = {
# 		"title" : "Nuevo Detalle Analisis",
# 		"form" : form,
# 	}
# 	return render(request, "alta_detAn.html", context)

# def v_detalleanalisis(request, id=None):
# 	if not request.user.is_authenticated() or request.user.is_staff:
# 		raise Http404
# 	instance = get_object_or_404(DetalleAnalisis, id=id)



# 	context = {
# 		"instance" : instance,
# 		"title": "Detalle de Analisis",
# 	}
# 	return render(request, "ver_detAn.html", context)

def u_detalleanalisis(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(DetalleAnalisis,id=id)
	form = DetalleAnalisisForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Detalle Analisis",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_detAn.html", context)

def d_detalleanalisis(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(DetalleAnalisis, id=id)
	instance.delete()
	return redirect("bsadmin:l_detalleanalisis")

# Detalle Analisis

def j_DetalleAnalisisPadre(request):
	queryset = DetalleAnalisisPadre.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_DetalleAnalisisPadreid(request,id=None):
	queryset = DetalleAnalisisPadre.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_DetalleAnalisisPadre(request):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	queryset = DetalleAnalisisPadre.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Detalle Analisis"
	}
	return render(request, "list_detAn.html", context)

def a_DetalleAnalisisPadre(request):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	form = DetalleAnalisisPadreForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Nuevo Detalle Analisis",
		"form" : form,
	}
	return render(request, "alta_detAn.html", context)

def v_DetalleAnalisisPadre(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	prot = instance.protocolo
	solic = instance.solicitud
	queryset = DetalleAnalisisPadre.objects.all().order_by('id').filter(protocolo=prot)
	# INSTANCIA_INDIVIDUOS
	queryset_Ind = DetalleAnalisis.objects.distinct('individuoPadre').filter(solicitud=solic)
	dict_ind={}
	for ind in queryset_Ind:
		k=ind
		det_ind = Individuos.objects.all().order_by('id').filter(padre=ind.individuoPadre)
		dict_ind[k]=det_ind
	#print(dict_ind)

	# hacer: por cada DAP {dap: estado}
	da_all = DetalleAnalisis.objects.all().filter(solicitud=solic)
	total=0
	completo=0
	vacio=0
	estado=""
	ter = Tercerizacion.objects.all().filter(detalleanalisispadre=instance)
	print(queryset)
	object_dict = {}
	for dap in queryset:
		k=dap
		if dap.diagnostico.tercerizacion or ter:
			if instance.diagnostico.tercerizacion:
				print("Tercerizado1")
				estado="Tercerizado1"
			if ter:
				print("Tercerizado2")
				estado="Tercerizado2"
		else:
			for da in da_all:
				if da.valor == "":
					completo=completo+1
				else:
					vacio=vacio+1
				total=total+1
			print("completo: "+str(completo)+", vacio: "+str(vacio)+", total: "+str(total))
			if vacio<completo:
				if total==completo:
					print("completo")
					estado="Completo"
				else:
					print("en proceso")
					estado="En Proceso"
			elif completo<=vacio:
				if total == vacio:
					print("vacio")
					estado="Vacío"
				else:
					print("en proceso")
					estado="En Proceso"
		object_dict[k]=estado
	print(object_dict)

	context = {
		"estado":estado,
		"dict_ind": dict_ind, #queryset_Ind,
		"object_dict": object_dict,
		"instance" : instance,
		"title": "Detalle de Analisis",
	}
	return render(request, "ver_detAn.html", context)

def u_DetalleAnalisisPadre(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(DetalleAnalisisPadre,id=id)
	# INSTANCIA_INDIVIDUOS
	# INSTANCIA_DIAGNOSTICO
	form = DetalleAnalisisPadreForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Detalle Analisis",
		"instance" : instance,
		# INSTANCIA_INDIVIDUOS
		# INSTANCIA_DIAGNOSTICO
		"form" : form,
	}
	return render(request, "alta_detAn.html", context)

""" # este view esta hecho como a_eliminacionprotocolo
def d_DetalleAnalisisPadre(request, id=None):
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	instance.delete()
	return redirect("bsadmin:l_DetalleAnalisisPadre")
"""
# Eliminacion Protocolo

def j_eliminacionprotocolo(request):
	queryset = EliminacionProtocolo.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_eliminacionprotocoloid(request,id=None):
	queryset = EliminacionProtocolo.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_eliminacionprotocolo(request):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	queryset = EliminacionProtocolo.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(protocolo__numero__icontains=query)

	paginator = Paginator(queryset, 15) # Show 25 DetAna_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		ElimProt_queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		ElimProt_queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		ElimProt_queryset = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,
		"object_list": ElimProt_queryset,
		"title": "Listado de Eliminacion Protocolos"
	}
	return render(request, "list_elimProt.html", context)

def a_eliminacionprotocolo(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	form = EliminacionProtocoloForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print(instance.protocolo.activo)
		instance.protocolo.activo = False
		instance.protocolo.save()
		print(instance.protocolo.activo)
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"instance" : instance,
		"title" : "Nuevo Eliminacion Protocolo",
		"form" : form,
	}
	return render(request, "alta_elimProt.html", context)

def v_eliminacionprotocolo(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(EliminacionProtocolo, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Eliminacion Protocolo",
	}
	return render(request, "ver_elimProt.html", context)

def u_eliminacionprotocolo(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance_ep = get_object_or_404(EliminacionProtocolo,id=id)
	dap_list = DetalleAnalisisPadre.objects.filter(protocolo=instance_ep.protocolo).distinct()
	for dap in dap_list:
		instance = dap
	form = EliminacionProtocoloForm(request.POST or None, instance=instance_ep)
	if form.is_valid():
		instance_ep = form.save(commit=False)
		instance_ep.save()
		return HttpResponseRedirect(instance_ep.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Eliminacion Protocolo",
		"instance" : instance,
		"instance_ep" : instance_ep,
		"form" : form,
	}
	return render(request, "alta_elimProt.html", context)

def d_eliminacionprotocolo(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(EliminacionProtocolo, id=id)
	instance.delete()
	return redirect("bsadmin:l_eliminacionprotocolo")

def activar_protocolo(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	instance.activo = True
	instance.save()
	instance.protocolo.activo = True
	instance.protocolo.save()
	ep_list = EliminacionProtocolo.objects.all().filter(protocolo=instance.protocolo)
	for ep in ep_list:
		ep.delete()
	return HttpResponseRedirect(instance.get_absolute_url())

# Tercerizar 

def j_tercerizar(request):
	queryset = Tercerizacion.objects.all().values().order_by('id')
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def j_tercerizarid(request,id=None):
	queryset = Tercerizacion.objects.filter(id=id).values()    
	queryset = list(queryset)  
	return JsonResponse(queryset, safe=False)

def l_tercerizar(request):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	queryset = Tercerizacion.objects.all().order_by('id')
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(detalleanalisispadre__protocolo__numero__icontains=query)

	paginator = Paginator(queryset, 15) # Show 25 Terc_queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		Terc_queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		Terc_queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		Terc_queryset = paginator.page(paginator.num_pages)

	context = {
		"page_request_var": page_request_var,	
		"object_list": Terc_queryset,
		"title": "Listado de Tercerización",
	}
	return render(request, "list_tercerizar.html", context)

def tercerizar(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	#traigo info de toda la solicitud de analisis
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	form = TercerizacionForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print(instance)
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Nueva Tercerización",
		"form" : form,
		"instance" : instance,
	}
	return render(request, "tercerizar.html", context)


"""
def a_tercerizar(request):
	form = TercerizacionForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Nueva Tercerización",
		"form" : form,
	}
	return render(request, "alta_tercerizar.html", context)
"""	
def v_tercerizar(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance = get_object_or_404(Tercerizacion, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Tercerización",
	}
	return render(request, "ver_tercerizar.html", context)


def u_tercerizar(request, idt=None, iddap=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	instance_t = get_object_or_404(Tercerizacion,id=idt)
	instance_dap = get_object_or_404(DetalleAnalisisPadre, id=iddap)
	form = TercerizacionForm(request.POST or None, instance=instance_t)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Tercerización",
		"instance_t" : instance_t,
		"instance": instance_dap,
		"form" : form,
	}
	return render(request, "u_tercerizar.html", context)

def hojadetrabajo(request, id=None):
	if not request.user.is_authenticated() or request.user.is_staff:
		raise Http404
	#traigo info de toda la solicitud de analisis
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	# traigo los parametros asociados al diagnostico
	diag = instance.diagnostico
	all_param_del_diag = Parametros.objects.all().filter(diagnostico=diag)
	# traigo los individuos asociados a la solicitud
	solic = instance.solicitud
	all_indiv_de_solic = DetalleAnalisis.objects.distinct('individuoPadre').filter(solicitud=solic)
	grupo_list_t = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="T")
	grupo_list_i = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="I")

	# trae un unico individuo para la parte del listar los ítmes una sola vez en el HTML	
	indi=0
	if all_indiv_de_solic:
		cant_indi = len(all_indiv_de_solic)
		indi = all_indiv_de_solic[cant_indi-1]

	# listado de valores de referencia filtrado por diag + param + especie
	vdr_all = ValoresReferencia.objects.all()
	vdr_list=[]
	for v in vdr_all:
		for p in all_param_del_diag:
			if v.parametros == p:
				if v.especie == instance.solicitud.especie:
					vdr_list.append(v)
	#print("vdr_list")
	#print(vdr_list)
	
	# listado de DetallesAnalisis como diccionario:
	# {Key: DA, Value: valor}
	da_all = DetalleAnalisis.objects.all().filter(solicitud=solic)
	da_list = {}
	for p in all_param_del_diag:
		for i in all_indiv_de_solic:
			for da in da_all:
				ban1=0
				if da.parametros == p:
					if da.individuoPadre == i.individuoPadre:
						if da.valor != '':
							#print("entro 1")
							valor=da.valor
							#print(linea)
							ban1=1
						else:
							for vdr in vdr_list:
								if vdr.parametros == p:
									#print("entro 2")
									valor=vdr.valorDef
									ban1=1
							if ban1==0:
								#print("entro 3")
								valor=""
								ban1=1
					da_list[da]=valor
	#print(da_list)

	# diccionario de grupos_tabla separados por rangos de a 5 parametros
	grupos = {}
	for g in grupo_list_t:
		cant=0
		for p in all_param_del_diag:
			if g.grupo == p.grupo:
				cant=cant+1
		inicio=0
		fin=5
		k=g.grupo
		list_r=[]
		ban=True
		while ban:
			rango= Parametros.objects.all().filter(diagnostico=diag, visualizacion1="T", grupo=k)[inicio:fin]
			#print("g rango  ", rango)
			list_r.append(rango)
			if fin < cant:
				#print(" ---entra al if-------- ")
				ban=True
				inicio = inicio+5
				fin = fin+5
			else:
				#print(" ---entra al else-------- ")
				ban=False
		grupos[k] = list_r
	#print(grupos)
	
	context = {
		"title" : "Registro de Resultados",
		"indi": indi,
		"da_list": da_list,
		"instance" : instance,
		"parametros_list" : all_param_del_diag,
		"object_list_ind": all_indiv_de_solic,
		"grupoi" : grupo_list_i,
		"grupos": grupos,
		"vdr_list": vdr_list, #listado de valores de referencia filtrados por parametro y especie

	}
	return render(request, "hojadetrabajo.html", context)


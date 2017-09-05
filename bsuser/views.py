from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from .models import *
from .forms import *
from django.core import serializers

# Create your views here.

def login(request):
	return render(request, "login.html")

def home_user(request):
	#DetAna_queryset = DetalleAnalisisPadre.objects.all().order_by('-protocolo')
	DetAna_queryset = DetalleAnalisisPadre.objects.distinct('protocolo')

	context = {
		"object_list": DetAna_queryset,
		"title": "Últimos Protocolos Registrados"
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

def l_solicitudanalisis(request):
	queryset = SolicitudAnalisis.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Solicitudes de Analisis"
	}
	return render(request, "list_solAn.html", context)

def a_solicitudanalisis(request):
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

def v_solicitudanalisis(request, id=None):
	instance = get_object_or_404(SolicitudAnalisis, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Solicitud de Analisis",
	}
	return render(request, "ver_solAn.html", context)

def u_solicitudanalisis(request, id=None):
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

def l_protocolo(request):
	queryset = Protocolo.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Protocolos"
	}
	return render(request, "list_protocolo.html", context)

def a_protocolo(request):
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

def l_individuopadre(request):
	queryset = IndividuoPadre.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Individuos Padre"
	}
	return render(request, "list_indivp.html", context)

def a_individuopadre(request):
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

def v_individuopadre(request, id=None):
	instance = get_object_or_404(IndividuoPadre, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Individuo Padre",
	}
	return render(request, "ver_indivp.html", context)

def u_individuopadre(request, id=None):
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

def l_individuos(request):
	queryset = Individuos.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Individuos"
	}
	return render(request, "list_indiv.html", context)

def a_individuos(request):
	form = IndividuosForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Nuevo Individuo",
		"form" : form,
	}
	return render(request, "alta_indiv.html", context)

def v_individuos(request, id=None):
	instance = get_object_or_404(Individuos, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Individuo",
	}
	return render(request, "ver_indiv.html", context)

def u_individuos(request, id=None):
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

def l_detalleanalisis(request):
	queryset = DetalleAnalisis.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Detalle Analisis"
	}
	return render(request, "list_detAn.html", context)

def a_detalleanalisis(request):
	form = DetalleAnalisisForm(request.POST or None)
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

def v_detalleanalisis(request, id=None):
	instance = get_object_or_404(DetalleAnalisis, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Analisis",
	}
	return render(request, "ver_detAn.html", context)

def u_detalleanalisis(request, id=None):
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
	queryset = DetalleAnalisisPadre.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Detalle Analisis"
	}
	return render(request, "list_detAn.html", context)

def a_DetalleAnalisisPadre(request):
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
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	prot = instance.protocolo
	queryset = DetalleAnalisisPadre.objects.all().order_by('id').filter(protocolo=prot)
	# INSTANCIA_INDIVIDUOS
	solic = instance.solicitud
	queryset_Ind = DetalleAnalisis.objects.all().order_by('id').filter(solicitud=solic)
	context = {
		"object_list_ind": queryset_Ind,
		"object_list": queryset,
		"instance" : instance,
			"title": "Detalle de Analisis",
	}
	return render(request, "ver_detAn.html", context)

def u_DetalleAnalisisPadre(request, id=None):
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
	queryset = EliminacionProtocolo.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Eliminacion Protocolos"
	}
	return render(request, "list_elimProt.html", context)

def a_eliminacionprotocolo(request, id=None):
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	form = EliminacionProtocoloForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
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
	instance = get_object_or_404(EliminacionProtocolo, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Eliminacion Protocolo",
	}
	return render(request, "ver_elimProt.html", context)

def u_eliminacionprotocolo(request, id=None):
	instance = get_object_or_404(EliminacionProtocolo,id=id)
	form = EliminacionProtocoloForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Eliminacion Protocolo",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_elimProt.html", context)

def d_eliminacionprotocolo(request, id=None):
	instance = get_object_or_404(EliminacionProtocolo, id=id)
	instance.delete()
	return redirect("bsadmin:l_eliminacionprotocolo")

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
	queryset = Tercerizacion.objects.all().order_by('id')
	context = {
		"object_list": queryset,
		"title": "Listado de Tercerización",
	}
	return render(request, "list_tercerizar.html", context)

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
def v_tercerizar(request, id=None):
	instance = get_object_or_404(Tercerizacion, id=id)
	context = {
		"instance" : instance,
		"title": "Detalle de Tercerización",
	}
	return render(request, "ver_tercerizar.html", context)


def u_tercerizar(request, id=None):
	instance = get_object_or_404(Tercerizacion,id=id)
	form = TercerizacionForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		print (form.errors)
	context = {
		"title" : "Modificar Tercerización",
		"instance" : instance,
		"form" : form,
	}
	return render(request, "alta_tercerizar.html", context)

def hojadetrabajo(request, id=None):
	#traigo info de toda la solicitud de analisis
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	# traigo los parametros asociados al diagnostico
	diag = instance.diagnostico
	queryset_Param = Parametros.objects.all().filter(diagnostico=diag)
	# traigo los individuos asociados a la solicitud
	solic = instance.solicitud
	queryset_Ind = DetalleAnalisis.objects.distinct('individuoPadre').filter(solicitud=solic)

	grupo_list_t = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="T")
	grupo_list_i = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="I")

	context = {
		"title" : "Hoja de Trabajo",
		"instance" : instance,
		"parametros_list" : queryset_Param,
		"object_list_ind": queryset_Ind,
		"grupot" : grupo_list_t,
		"grupoi" : grupo_list_i,

	}
	return render(request, "hojadetrabajo.html", context)

def tercerizar(request, id=None):
	#traigo info de toda la solicitud de analisis
	instance_dap = get_object_or_404(DetalleAnalisisPadre, id=id)
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
		"instance" : instance_dap,
	}
	return render(request, "tercerizar.html", context)


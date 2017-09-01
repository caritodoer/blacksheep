from django import forms
from .models import *

class SolicitudAnalisisForm(forms.ModelForm):
	class Meta:
		model = SolicitudAnalisis
		fields = [
			"veterinario",
			"establecimiento",
			"motivo",
			"especie",
			"fecha",
			"obs",
			"activo",
		]

class ProtocoloForm(forms.ModelForm):
	class Meta:
		model = Protocolo
		fields = [
			"numero",
			"activo",
		]

class IndividuoPadreForm(forms.ModelForm):
	class Meta:
		model = IndividuoPadre
		fields = [
			"identificacion",
			"raza",
		]

class IndividuosForm(forms.ModelForm):
	class Meta:
		model = Individuos
		fields = [
			"padre",
			"nombre",
			"edad",
			"sexo",
			"libretasanitaria",
			"categoriae",
		]

class DetalleAnalisisFormPadre(forms.ModelForm):
	class Meta:
		model = DetalleAnalisisPadre
		fields = [
			"solicitud",
			"protocolo",
			"diagnostico"
		]

class DetalleAnalisisForm(forms.ModelForm):
	class Meta:
		model = DetalleAnalisis
		fields = [
			# "padre",
			"solicitud",
			"individuo",
			"parametros",
			"valor"
		]

class EliminacionProtocoloForm(forms.ModelForm):
	class Meta:
		model = EliminacionProtocolo
		fields = [
			"protocolo",
			"fecha",
			"motivoBaja",
			#"usuario",
		]

class TercerizarForm(forms.ModelForm):
	class Meta:
		model = Tercerizar
		fields = [
			"fecha_envio",
			"fecha_devolucion",
			"institucion",
			"detalleanalisispadre"
		]
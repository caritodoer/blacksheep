from django import forms
from .models import *


class EspecializacionForm(forms.ModelForm):
	class Meta:
		model = Especializacion
		fields = [
			"descripcion",
		]

		
class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = [
			"descripcion",
		]

class MotivosForm(forms.ModelForm):
	class Meta:
		model = Motivos
		fields = [
			"descripcion", 
		]

class EspecieForm(forms.ModelForm):
	class Meta:
		model = Especie
		fields = [
			"descripcion",
		]

class MuestraForm(forms.ModelForm):
	class Meta:
		model = Muestra
		fields = [
			"descripcion",
		]

class ExplotacionForm(forms.ModelForm):
	class Meta:
		model = Explotacion
		fields = [
			"descripcion"
		]			

class CategoriaEForm(forms.ModelForm):
	class Meta:
		model = CategoriaE
		fields = [
			"descripcion",
			"especie"
		]

class RazaForm(forms.ModelForm):
	class Meta:
		model = Raza
		fields = [
			"descripcion",
			"especie"
		]

class ParametrosForm(forms.ModelForm):
	class Meta:
		model = Parametros
		fields = [
			"diagnostico",
			"descripcion",
			"tipo_de_dato",
			"unidadmedida",
			"grupo"
		]	

class DiagnosticoForm(forms.ModelForm):
	class Meta:
		model = Diagnostico
		fields = [
			"descripcion",
			"tecnica",
			"muestra",
			"tercerizacion",
			"activo",
			"piepagina"	
		]

class ParametrosForm(forms.ModelForm):
	class Meta:
		model = Parametros
		fields = [
			"diagnostico",
			"descripcion",
			"tipo_de_dato",
			"unidadmedida",
			"grupo"
		]
			
class ValoresReferenciaForm(forms.ModelForm):
	class Meta:
		model = ValoresReferencia
		fields = [
			"especie",
			"parametros",
			"valorRef",
			"valorDef"
		]


class VeterinarioForm(forms.ModelForm):
	especializaciones = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Especializacion.objects.all())
	class Meta:
		model = Veterinario
		fields = [
			"nombre",
			"apellido",
			"matricula",
			"dni",
			"domicilio_particular",
			"cp_domicilio_particular",
			"domicilio_fiscal",
			"cp_domicilio_fiscal",
			"email",
			"cuit",
			"codigo_area",
			"telefono1",
			"telefono2",
			"fecha_ingreso",
			"fecha_baja",
			"acreditacion_brucelosis",
			"acreditacion_aie",
			"especializaciones",
			"activo"
		]

class EstablecimientoForm(forms.ModelForm):
	categorias = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Categoria.objects.all())
	explotacion = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Explotacion.objects.all())
	
	class Meta:
		model = Establecimiento
		fields = [
			"nombre",
			"partido",
			"propietario",
			"RENSPA",
			"CUIT",
			"veterinario",
			"categorias",
			"explotacion",
			"activo"
		]
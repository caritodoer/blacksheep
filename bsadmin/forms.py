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
			"descripcion" 
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

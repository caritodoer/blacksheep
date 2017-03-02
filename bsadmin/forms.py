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

class EspecieForm(forms.ModelForm):
	class Meta:
		model = Especie
		fields = [
			"descripcion",
		]
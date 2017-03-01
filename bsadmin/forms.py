from django import forms
from .models import *


class EspecializacionForm(forms.ModelForm):
	class Meta:
		model = Especializacion
		fields = [
			"descripcion",
		]
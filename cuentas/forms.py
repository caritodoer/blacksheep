from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from crispy_forms.helper import FormHelper

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("El nombre de Usuario no es correcto.")

			if not user.check_password(password):
				raise forms.ValidationError("La contraseña no es correcta.")

			if not user.is_active:
				raise forms.ValidationError("Este Usuario ya no esta activo.")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email')
	email2 = forms.EmailField(label='Confirme Email')
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email',
			'email2',
		]
	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("El e-mail no coincide")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Este email ya fue registrado")

		return email

	

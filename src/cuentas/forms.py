from django import forms
from django.contrib.auth.models import User


class RegistroUsuarioForm(forms.Form):
	username = forms.CharField(label='Nombre de usuario',min_length=3)
	email = forms.EmailField()
	password = forms.CharField(label='Contraseña',min_length=1, widget=forms.PasswordInput())
	password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username):
			raise forms.ValidationError('Ya existe un usuario registrado con ese nombre')
		return username

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError('Ya existe un usuario registrado con ese email')
		return email

	def clean_password2(self):
		password2 = self.cleaned_data['password2']
		password = self.cleaned_data['password']
		if password != password2:
			raise forms.ValidationError('Las contraseñas no coinciden')
		return password2

class EditarEmailForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput())

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request')
		return super().__init__(*args,**kwargs)

	def clean_email(self):
		email = self.cleaned_data['email']
		actual_email = self.request.user.email
		username = self.request.user.username
		if email != actual_email:
			existe = User.objects.filter(email=email).exclude(username=username)
			if existe:
				raise forms.ValidationError('Ya existe un email igual en la base de datos')
		return email

class EditarContrasenaForm(forms.Form):

    actual_password = forms.CharField(label='Contraseña actual',min_length=1,widget=forms.PasswordInput())

    password = forms.CharField(label='Nueva contraseña',min_length=4,widget=forms.PasswordInput())

    password2 = forms.CharField(label='Repetir contraseña',min_length=4,widget=forms.PasswordInput())

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2


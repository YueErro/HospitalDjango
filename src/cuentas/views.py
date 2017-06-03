from django.shortcuts import render
from .forms import (RegistroUsuarioForm,EditarEmailForm,EditarContrasenaForm)
from .models import UserProfile
from pacientes.models import PacienteProfile

from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import make_password

def registro_usuario_view(request):
	if request.method == 'POST':
		form = RegistroUsuarioForm(request.POST, request.FILES)

		if form.is_valid():
			cleaned_data = form.cleaned_data
			username = cleaned_data.get('username')
			password = cleaned_data.get('password')
			email = cleaned_data.get('email')
			
			user_model = User.objects.create_user(username=username,password=password)
			user_model.email = email
			user_model.save()
			user_profile = UserProfile()
			user_profile.user = user_model
			user_profile.save()
		
			return redirect(reverse('cuentas.gracias', kwargs={'username':username}))

	else:
		form = RegistroUsuarioForm()
	context = {
		'form' : form
	}
	return render(request, 'cuentas/registro.html', context)


def gracias_view(request, username):
	return render(request, 'cuentas/gracias.html', {'username':username})

@login_required
def index_view(request):
	res = PacienteProfile.objects.filter(usuario=request.user.username)
	return render(request, 'cuentas/index.html', {'res':res})

def login_view(request):
	if request.user.is_authenticated():
		return redirect(reverse('cuentas.index'))

	mensaje= ""
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		reg = request.POST.get('reg')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:

				login(request,user)
				return redirect(reverse('cuentas.index'))

			else:
				pass
		mensaje= "Nombre de usuario o contraseña incorrectos"
	return render(request,'cuentas/login.html',{'mensaje':mensaje})

def logout_view(request):
	logout(request)
	messages.success(request, 'Te has desconectado de Servicio Salud con exito')
	return redirect(reverse('cuentas.login'))

@login_required
def editar_email(request):
	if request.method == "POST":
		form = EditarEmailForm(request.POST,request=request)
		if form.is_valid():
			request.user.email = form.cleaned_data['email']
			request.user.save()
			messages.success(request,'El email se ha cambiado corectamente')
			return redirect(reverse('cuentas.index'))
	else:
		form = EditarEmailForm(request=request, initial={'email': request.user.email})
	return render(request,'cuentas/editar_email.html',{'form':form})

@login_required
def editar_contrasena(request):
	if request.method == 'POST':
       		form = EditarContrasenaForm(request.POST)
        	if form.is_valid():
            		request.user.password = make_password(form.cleaned_data['password'])
            		request.user.save()
            		messages.success(request, 'La contraseña ha sido cambiada')
            		return redirect(reverse('cuentas.index'))
	else:
        	form = EditarContrasenaForm()
	return render(request, 'cuentas/editar_contrasena.html', {'form': form})



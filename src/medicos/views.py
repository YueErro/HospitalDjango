from django.shortcuts import render
from pacientes.models import PacienteProfile
from django.shortcuts import redirect

from .forms import RespuestaPaciente
from .models import Respuesta

from django.core.urlresolvers import reverse

from django.contrib import messages
from django.db import connection


def ver_enfermedades_view(request):
	enfermos = PacienteProfile.objects.all()
	nEnf = len(enfermos)

	cursor = connection.cursor()

	usuario = cursor.execute('select reg from auth_user where email="' + request.user.email + '"')
	result = str(cursor.fetchone()[0])

	if result != 'medico':
		res = PacienteProfile.objects.filter(usuario=request.user.username)
		messages.success(request, 'No puedes acceder a esta página')
		return render(request, 'cuentas/index.html', {'res':res})
	else:
		return render(request, 'medicos/ver.html', {'enfermos':enfermos, 'nEnf':nEnf})

def ver_enfermo_view(request,e_id):
	enfermo = PacienteProfile.objects.filter(id=e_id)
	enfermos = PacienteProfile.objects.all()
	nEnf = len(enfermos)
	cursor = connection.cursor()
	form = RespuestaPaciente(request.POST, request.FILES)
	if form.is_valid():
		cleaned_data = form.cleaned_data
		respuesta = cleaned_data.get('respuesta')
		id = cleaned_data.get('id')
		cursor.execute('update pacientes_pacienteprofile set respuesta="'+ respuesta+ '" where id=' + e_id)

		return render(request, 'medicos/ver.html', {'enfermos':enfermos, 'nEnf':nEnf})
	else:
		form = RespuestaPaciente()
	context = {
		'form' : form
	}
	return render(request, 'medicos/veruna.html', {'enfermo':enfermo})
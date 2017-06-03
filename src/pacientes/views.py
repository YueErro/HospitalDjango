from django.shortcuts import render
from .forms import RegistroPacienteForm
from .models import PacienteProfile

from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.db import connection

def registro_paciente_view(request):
	
	cursor = connection.cursor()

	usuario = cursor.execute('select reg from auth_user where email="' + request.user.email + '"')
	result = str(cursor.fetchone()[0])

	if result == 'medico':
		messages.success(request, 'No puedes acceder a esta página')
		return render(request, 'cuentas/index.html')
	else:
		if request.method == 'POST':
			form = RegistroPacienteForm(request.POST, request.FILES)

			if form.is_valid():
				cleaned_data = form.cleaned_data
				username = request.user.username
				nombre = cleaned_data.get('nombre')
				pais = cleaned_data.get('pais')
				ciudad = cleaned_data.get('ciudad')
				domicilio = cleaned_data.get('domicilio')
				edad = cleaned_data.get('edad')
				sexo = cleaned_data.get('sexo')
				Area_Medica = cleaned_data.get('Area_Medica')
				Reporte_Enfermedad = cleaned_data.get('Reporte_Enfermedad')
				Foto = cleaned_data.get('Foto')
				Dias_enfermo = cleaned_data.get('Dias_enfermo')
				Comentarios = cleaned_data.get('Comentarios')

				paciente_prof = PacienteProfile()
				paciente_prof.pais = pais
				paciente_prof.edad = edad
				paciente_prof.nombre = nombre
				paciente_prof.ciudad = ciudad
				paciente_prof.Reporte_Enfermedad  = Reporte_Enfermedad
				paciente_prof.Foto = Foto
				paciente_prof.Dias_enfermo = Dias_enfermo
				paciente_prof.sexo  = sexo
				paciente_prof.domicilio = domicilio
				paciente_prof.Area_Medica  = Area_Medica
				paciente_prof.domicilio = domicilio
				paciente_prof.usuario = username
				paciente_prof.Comentarios = Comentarios

				paciente_prof.save()
			
				return redirect(reverse('pacientes.gracias', kwargs={'username':username}))

		else:
			form = RegistroPacienteForm()
		context = {
			'form' : form
		}
		

		return render(request, 'pacientes/registro.html', context)


def gracias_view(request, username):
	return render(request, 'pacientes/gracias.html', {'username':username})

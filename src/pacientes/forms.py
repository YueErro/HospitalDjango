from django import forms
from django.contrib.auth.models import User


sex = [('Masculino','Masculino'),('Femenino','Femenino')]
Area_Medic = [('Aparato respiratorio','Aparato respiratorio'),('Cardiovascular','Cardiovascular'),('Endocrino','Endocrino'),('Digestivo','Digestivo'),('Neurología','Neurología'),('Oncología','Oncología')]

class RegistroPacienteForm(forms.Form):
	nombre = forms.CharField(min_length=3)
	pais = forms.CharField(min_length=4)
	ciudad = forms.CharField(min_length=4)
	domicilio = forms.CharField(min_length=4)
	edad = forms.IntegerField(min_value=1)
	sexo = forms.ChoiceField(choices=sex)
	Area_Medica = forms.ChoiceField(choices=Area_Medic)
	Reporte_Enfermedad = forms.CharField(min_length=4)
	Foto = forms.URLField(label='Foto')
	Dias_enfermo = forms.IntegerField(min_value=1)
	Archivos = forms.FileField(label='Subir archivos', required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
	Comentarios = forms.CharField(widget=forms.Textarea)

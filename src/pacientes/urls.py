from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^registro/$', views.registro_paciente_view, name='pacientes.registro'),
	url(r'gracias/(?P<username>[\w]+)/$', views.gracias_view, name='pacientes.gracias'),
]
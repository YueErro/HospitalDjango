from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^ver/$', views.ver_enfermedades_view, name='medicos.ver'),
	url(r'^enfermo/(?P<e_id>\d+)$', views.ver_enfermo_view, name='medicos.enfermo'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^registro/$', views.registro_usuario_view, name='cuentas.registro'),
	url(r'gracias/(?P<username>[\w]+)/$', views.gracias_view, name='cuentas.gracias'),
	url(r'^login/$',views.login_view, name='cuentas.login'),
	url(r'^$', views.index_view, name='cuentas.index'),
	url(r'^logout/$', views.logout_view, name='cuentas.logout'),
	url(r'^editar_email/$', views.editar_email, name='cuentas.editar_email'),
	url(r'^editar_contrasena/$', views.editar_contrasena, name='cuentas.editar_contrasena'),
	
]
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('^', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls')),
    url(r'^cuentas/', include('cuentas.urls')),
    url(r'^pacientes/', include('pacientes.urls')),
    url(r'^medicos/', include('medicos.urls')),
]

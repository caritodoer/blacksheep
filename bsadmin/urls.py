from django.conf.urls import url
from django.contrib import admin
from bsadmin import views

# l: listado
# a: alta
# v: ver
# u: update
# d: delete

urlpatterns = [
	# Veterinario
    url(r'^veterinario/$', views.l_veterinario),
    
    # Categoria
    url(r'^categoria/$', views.l_categoria),
    
    # Explotacion
    url(r'^explotacion/$', views.l_explotacion),
    
    # Especie
    url(r'^especie/$', views.l_especie),
    
    # Muestra
    url(r'^muestra/$', views.l_muestra),
    
    # Especializacion
    url(r'^especializacion/$', views.l_especializacion, name="l_especializacion"),
    url(r'^especializacion/alta/$', views.a_especializacion),
    url(r'^especializacion/(?P<id>\d+)/$', views.v_especializacion, name="v_especializacion"),
    url(r'^especializacion/update/(?P<id>\d+)/$', views.u_especializacion),
    url(r'^especializacion/delete/(?P<id>\d+)/$', views.d_especializacion),
    
    # Establecimiento
    url(r'^establecimiento/$', views.l_establecimiento),
]

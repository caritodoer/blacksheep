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
    url(r'^categoria/$', views.l_categoria, name="l_categoria"),
    url(r'^categoria/alta/$', views.a_categoria),
    url(r'^categoria/(?P<id>\d+)/$', views.v_categoria, name="v_categoria"),
    url(r'^categoria/update/(?P<id>\d+)/$', views.u_categoria),
    url(r'^categoria/delete/(?P<id>\d+)/$', views.d_categoria),

    ##explotacion
    url(r'^explotacion/$', views.l_explotacion, name='l_explotacion'),##listado
    url(r'^explotacion/alta$', views.a_explotacion),##alta
    url(r'^explotacion/(?P<id>\d+)/$', views.v_explotacion, name='v_explotacion'),##detalle
    url(r'^explotacion/update/(?P<id>\d+)/$', views.u_explotacion ),##modificacion
    url(r'^explotacion/delete/(?P<id>\d+)/$', views.d_explotacion ),##eliminar  
    
    # Especie
    url(r'^especie/$', views.l_especie, name="l_especie"),
    url(r'^especie/alta/$', views.a_especie),
    url(r'^especie/(?P<id>\d+)/$', views.v_especie, name="v_especie"),
    url(r'^especie/update/(?P<id>\d+)/$', views.u_especie),
    url(r'^especie/delete/(?P<id>\d+)/$', views.d_especie),
    
    # Muestra
    url(r'^muestra/$', views.l_muestra),

    
    # MOTIVOS

    url(r'^motivos/$', views.l_motivos, name="l_motivos"),
    url(r'^motivos/alta$', views.a_motivos),
    url(r'^motivos/(?P<id>\d+)/$', views.v_motivos, name="v_motivos"),
    url(r'^motivos/update/(?P<id>\d+)/$', views.u_motivos),
    url(r'^motivos/delete/(?P<id>\d+)/$', views.d_motivos),    

    
    # Especializacion
    url(r'^especializacion/$', views.l_especializacion, name="l_especializacion"),
    url(r'^especializacion/alta/$', views.a_especializacion),
    url(r'^especializacion/(?P<id>\d+)/$', views.v_especializacion, name="v_especializacion"),
    url(r'^especializacion/update/(?P<id>\d+)/$', views.u_especializacion),
    url(r'^especializacion/delete/(?P<id>\d+)/$', views.d_especializacion),
    
    # Establecimiento
    url(r'^establecimiento/$', views.l_establecimiento),
]

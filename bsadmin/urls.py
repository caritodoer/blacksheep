from django.conf.urls import url
from django.contrib import admin
from bsadmin import views

# l: listado
# a: alta
# v: ver
# u: update
# d: delete

urlpatterns = [
    

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
    url(r'^muestra/$', views.l_muestra, name="l_muestra"),
    url(r'^muestra/alta/$', views.a_muestra),
    url(r'^muestra/(?P<id>\d+)/$', views.v_muestra, name="v_muestra"),
    url(r'^muestra/update/(?P<id>\d+)/$', views.u_muestra),
    url(r'^muestra/delete/(?P<id>\d+)/$', views.d_muestra),    
    
    # MOTIVOS

    url(r'^motivos/$', views.l_motivos, name="l_motivos"),
    url(r'^motivos/alta$', views.a_motivos),
    url(r'^motivos/(?P<id>\d+)/$', views.v_motivos, name="v_motivos"),
    url(r'^motivos/update/(?P<id>\d+)/$', views.u_motivos),
    url(r'^motivos/delete/(?P<id>\d+)/$', views.d_motivos),    


    # categoriae
    url(r'^categoriae/$', views.l_categoriae, name="l_categoriae"),
    url(r'^categoriae/alta/$', views.a_categoriae),
    url(r'^categoriae/(?P<id>\d+)/$', views.v_categoriae, name="v_categoriae"),
    url(r'^categoriae/update/(?P<id>\d+)/$', views.u_categoriae),
    url(r'^categoriae/delete/(?P<id>\d+)/$', views.d_categoriae),
    

    # Especializacion
    url(r'^especializacion/$', views.l_especializacion, name="l_especializacion"),
    url(r'^especializacion/alta/$', views.a_especializacion),
    url(r'^especializacion/(?P<id>\d+)/$', views.v_especializacion, name="v_especializacion"),
    url(r'^especializacion/update/(?P<id>\d+)/$', views.u_especializacion),
    url(r'^especializacion/delete/(?P<id>\d+)/$', views.d_especializacion),
    
    # raza
    url(r'^raza/$', views.l_raza, name="l_raza"),
    url(r'^raza/alta/$', views.a_raza),
    url(r'^raza/(?P<id>\d+)/$', views.v_raza, name="v_raza"),
    url(r'^raza/update/(?P<id>\d+)/$', views.u_raza),
    url(r'^raza/delete/(?P<id>\d+)/$', views.d_raza),

    # parametros
    url(r'^parametros/$', views.l_parametros, name="l_parametros"),
    url(r'^parametros/alta/$', views.a_parametros),
    url(r'^parametros/(?P<id>\d+)/$', views.v_parametros, name="v_parametros"),
    url(r'^parametros/update/(?P<id>\d+)/$', views.u_parametros),
    url(r'^parametros/delete/(?P<id>\d+)/$', views.d_parametros),

    # diagnostico
    url(r'^diagnostico/$', views.l_diagnostico, name="l_diagnostico"),
    url(r'^diagnostico/alta/$', views.a_diagnostico),
    url(r'^diagnostico/(?P<id>\d+)/$', views.v_diagnostico, name="v_diagnostico"),
    url(r'^diagnostico/update/(?P<id>\d+)/$', views.u_diagnostico),
    url(r'^diagnostico/delete/(?P<id>\d+)/$', views.d_diagnostico),

    # valoresreferencia
    url(r'^valoresreferencia/$', views.l_valoresreferencia, name="l_valoresreferencia"),
    url(r'^valoresreferencia/alta/$', views.a_valoresreferencia),
    url(r'^valoresreferencia/(?P<id>\d+)/$', views.v_valoresreferencia, name="v_valoresreferencia"),
    url(r'^valoresreferencia/update/(?P<id>\d+)/$', views.u_valoresreferencia),
    url(r'^valoresreferencia/delete/(?P<id>\d+)/$', views.d_valoresreferencia),


    # veterinario
    url(r'^veterinario/$', views.l_veterinario, name="l_veterinario"),
    url(r'^veterinario/alta/$', views.a_veterinario),
    url(r'^veterinario/(?P<id>\d+)/$', views.v_veterinario, name="v_veterinario"),
    url(r'^veterinario/update/(?P<id>\d+)/$', views.u_veterinario),
    url(r'^veterinario/delete/(?P<id>\d+)/$', views.d_veterinario),


    # Establecimiento
    url(r'^establecimiento/$', views.l_establecimiento),
]

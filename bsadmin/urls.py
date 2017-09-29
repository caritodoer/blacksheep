from django.conf.urls import url
from django.contrib import admin
from bsadmin import views

# l: listado
# a: alta
# v: ver
# u: update
# d: delete
# j: json

urlpatterns = [
    url(r'^home_admin/$', views.home_admin, name="home_admin"),

    #Diagnostico Ajax
    url(r'^diagnosticoAjax/$', views.diagnosticoAjax),
    url(r'^parametrosAjax/$', views.parametrosAjax),
    url(r'^valRefAjax/$', views.valRefAjax),
    
    # Categoria
    url(r'^categoria/$', views.l_categoria, name="l_categoria"),
    url(r'^categoria/alta/$', views.a_categoria),
    url(r'^categoria/(?P<id>\d+)/$', views.v_categoria, name="v_categoria"),
    url(r'^categoria/update/(?P<id>\d+)/$', views.u_categoria),
    url(r'^categoria/delete/(?P<id>\d+)/$', views.d_categoria),
    url(r'^categoria/activar/(?P<id>\d+)/$', views.activar_categoria),
    url(r'^j_categoria/$', views.j_categoria),
    url(r'^j_categoriaid/(?P<id>\d+)/$', views.j_categoriaid),

    ##explotacion
    url(r'^explotacion/$', views.l_explotacion, name='l_explotacion'),##listado
    url(r'^explotacion/alta$', views.a_explotacion),##alta
    url(r'^explotacion/(?P<id>\d+)/$', views.v_explotacion, name='v_explotacion'),##detalle
    url(r'^explotacion/update/(?P<id>\d+)/$', views.u_explotacion ),##modificacion
    url(r'^explotacion/delete/(?P<id>\d+)/$', views.d_explotacion ),##eliminar  
    url(r'^explotacion/activar/(?P<id>\d+)/$', views.activar_explotacion ),
    url(r'^j_explotacion/$', views.j_explotacion),
    url(r'^j_explotacionid/(?P<id>\d+)/$', views.j_explotacionid),

    # Especie
    url(r'^especie/$', views.l_especie, name="l_especie"),
    url(r'^especie/alta/$', views.a_especie),
    url(r'^especie/(?P<id>\d+)/$', views.v_especie, name="v_especie"),
    url(r'^especie/update/(?P<id>\d+)/$', views.u_especie),
    url(r'^especie/delete/(?P<id>\d+)/$', views.d_especie),
    url(r'^especie/activar/(?P<id>\d+)/$', views.activar_especie),
    url(r'^j_especie/$', views.j_especie),
    url(r'^j_especieid/(?P<id>\d+)/$', views.j_especieid),

    # Muestra
    url(r'^muestra/$', views.l_muestra, name="l_muestra"),
    url(r'^muestra/alta/$', views.a_muestra),
    url(r'^muestra/(?P<id>\d+)/$', views.v_muestra, name="v_muestra"),
    url(r'^muestra/update/(?P<id>\d+)/$', views.u_muestra),
    url(r'^muestra/delete/(?P<id>\d+)/$', views.d_muestra),
    url(r'^muestra/activar/(?P<id>\d+)/$', views.activar_muestra),    
    url(r'^j_muestra/$', views.j_muestra),
    url(r'^j_muestraid/(?P<id>\d+)/$', views.j_muestraid),

    # MOTIVOS
    url(r'^motivos/$', views.l_motivos, name="l_motivos"),
    url(r'^motivos/alta/$', views.a_motivos),
    url(r'^motivos/(?P<id>\d+)/$', views.v_motivos, name="v_motivos"),
    url(r'^motivos/update/(?P<id>\d+)/$', views.u_motivos),
    url(r'^motivos/delete/(?P<id>\d+)/$', views.d_motivos),
    url(r'^motivos/activar/(?P<id>\d+)/$', views.activar_motivos),
    url(r'^j_motivos/$', views.j_motivos),
    url(r'^j_motivosid/(?P<id>\d+)/$', views.j_motivosid),

    # Raza
    url(r'^raza/$', views.l_raza, name="l_raza"),
    url(r'^raza/alta/$', views.a_raza),
    url(r'^raza/(?P<id>\d+)/$', views.v_raza, name="v_raza"),
    url(r'^raza/update/(?P<id>\d+)/$', views.u_raza),
    url(r'^raza/delete/(?P<id>\d+)/$', views.d_raza),
    url(r'^raza/activar/(?P<id>\d+)/$', views.activar_raza),        
    url(r'^j_raza/$', views.j_raza),
    url(r'^j_razaid/(?P<id>\d+)/$', views.j_razaid),

    # categoriae
    url(r'^categoriae/$', views.l_categoriae, name="l_categoriae"),
    url(r'^categoriae/alta/$', views.a_categoriae),
    url(r'^categoriae/(?P<id>\d+)/$', views.v_categoriae, name="v_categoriae"),
    url(r'^categoriae/update/(?P<id>\d+)/$', views.u_categoriae),
    url(r'^categoriae/delete/(?P<id>\d+)/$', views.d_categoriae),
    url(r'^categoriae/activar/(?P<id>\d+)/$', views.activar_categoriae),
    url(r'^j_categoriae/$', views.j_categoriae),
    url(r'^j_categoriaeid/(?P<id>\d+)/$', views.j_categoriaeid),

    # Especializacion
    url(r'^especializacion/$', views.l_especializacion, name="l_especializacion"),
    url(r'^especializacion/alta/$', views.a_especializacion),
    url(r'^especializacion/(?P<id>\d+)/$', views.v_especializacion, name="v_especializacion"),
    url(r'^especializacion/update/(?P<id>\d+)/$', views.u_especializacion),
    url(r'^especializacion/delete/(?P<id>\d+)/$', views.d_especializacion),
    url(r'^especializacion/activar/(?P<id>\d+)/$', views.activar_especializacion),
    url(r'^j_especializacion/$', views.j_especializacion),
    url(r'^j_especializacionid/(?P<id>\d+)/$', views.j_especializacionid),

    # parametros
    url(r'^parametros/$', views.l_parametros, name="l_parametros"),
    url(r'^parametros/alta/$', views.a_parametros),
    url(r'^parametros/(?P<id>\d+)/$', views.v_parametros, name="v_parametros"),
    url(r'^parametros/update/(?P<id>\d+)/$', views.u_parametros),
    url(r'^parametros/delete/(?P<id>\d+)/$', views.d_parametros),
    url(r'^parametros/activar/(?P<id>\d+)/$', views.activar_parametros),
    url(r'^j_parametros/$', views.j_parametros),
    url(r'^j_parametrosid/(?P<id>\d+)/$', views.j_parametrosid),

    # diagnostico
    url(r'^diagnostico/$', views.l_diagnostico, name="l_diagnostico"),
    url(r'^diagnostico/alta/$', views.a_diagnostico),
    url(r'^diagnostico/(?P<id>\d+)/$', views.v_diagnostico, name="v_diagnostico"),
    url(r'^diagnostico/update/(?P<id>\d+)/$', views.u_diagnostico),
    url(r'^diagnostico/delete/(?P<id>\d+)/$', views.d_diagnostico),
    url(r'^diagnostico/activar/(?P<id>\d+)/$', views.activar_diagnostico),
    url(r'^j_diagnostico/$', views.j_diagnostico),
    url(r'^j_diagnosticoid/(?P<id>\d+)/$', views.j_diagnosticoid),

    # valoresreferencia
    url(r'^valoresreferencia/$', views.l_valoresreferencia, name="l_valoresreferencia"),
    url(r'^valoresreferencia/alta/$', views.a_valoresreferencia),
    url(r'^valoresreferencia/(?P<id>\d+)/$', views.v_valoresreferencia, name="v_valoresreferencia"),
    url(r'^valoresreferencia/update/(?P<id>\d+)/$', views.u_valoresreferencia),
    url(r'^valoresreferencia/delete/(?P<id>\d+)/$', views.d_valoresreferencia),
    url(r'^valoresreferencia/activar/(?P<id>\d+)/$', views.activar_valoresreferencia),
    url(r'^j_valoresreferencia/$', views.j_valoresreferencia),
    url(r'^j_valoresreferenciaid/(?P<id>\d+)/$', views.j_valoresreferenciaid),

    # veterinario
    url(r'^veterinario/$', views.l_veterinario, name="l_veterinario"),
    url(r'^veterinario/alta/$', views.a_veterinario),
    url(r'^veterinario/(?P<id>\d+)/$', views.v_veterinario, name="v_veterinario"),
    url(r'^veterinario/update/(?P<id>\d+)/$', views.u_veterinario),
    url(r'^veterinario/delete/(?P<id>\d+)/$', views.d_veterinario),
    url(r'^veterinario/activar/(?P<id>\d+)/$', views.activar_veterinario),
    url(r'^j_veterinario/$', views.j_veterinario),
    url(r'^j_veterinarioid/(?P<id>\d+)/$', views.j_veterinarioid),

    # establecimiento
    url(r'^establecimiento/$', views.l_establecimiento, name="l_establecimiento"),
    url(r'^establecimiento/alta/$', views.a_establecimiento),
    url(r'^establecimiento/(?P<id>\d+)/$', views.v_establecimiento, name="v_establecimiento"),
    url(r'^establecimiento/update/(?P<id>\d+)/$', views.u_establecimiento),
    url(r'^establecimiento/delete/(?P<id>\d+)/$', views.d_establecimiento),
    url(r'^establecimiento/activar/(?P<id>\d+)/$', views.activar_establecimiento),
    url(r'^j_establecimiento/$', views.j_establecimiento),
    url(r'^j_establecimientoid/(?P<id>\d+)/$', views.j_establecimientoid),

    # empresa
    url(r'^empresa/update/(?P<id>\d+)/$', views.u_empresa),
    url(r'^empresa/alta/$', views.a_empresa),
    
]

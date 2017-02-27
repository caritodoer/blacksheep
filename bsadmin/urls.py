from django.conf.urls import url
from django.contrib import admin
from bsadmin import views


urlpatterns = [
	## urls de listados
    url(r'^lista_veterinario/$', views.l_veterinario),
    url(r'^lista_categoria/$', views.l_categoria),
    url(r'^lista_explotacion/$', views.l_explotacion),
    url(r'^lista_especie/$', views.l_especie),
    url(r'^lista_muestra/$', views.l_muestra),
    url(r'^lista_establecimiento/$', views.l_establecimiento),

    ## urls de altas


    ## urls de modificacion


    ## urls de eliminacion
]

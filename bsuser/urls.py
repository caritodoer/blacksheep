from django.conf.urls import url
from django.contrib import admin
from bsuser import views

# l: listado
# a: alta
# v: ver
# u: update
# d: delete
# j: json

urlpatterns = [
	url(r'^$', views.login),
    url(r'^home_user/$', views.home_user),

    # Solicitud Analisis
    url(r'^solicitudanalisis/$', views.l_solicitudanalisis, name="l_solicitudAnalisis"),
    url(r'^solicitudanalisis/alta/$', views.a_solicitudanalisis),
    url(r'^solicitudanalisis/(?P<id>\d+)/$', views.v_solicitudanalisis, name="v_solicitudAnalisis"),
    url(r'^solicitudanalisis/update/(?P<id>\d+)/$', views.u_solicitudanalisis),
    url(r'^solicitudanalisis/delete/(?P<id>\d+)/$', views.d_solicitudanalisis),
    url(r'^j_solicitudanalisis/$', views.j_solicitudanalisis),
    url(r'^j_solicitudanalisisid/(?P<id>\d+)/$', views.j_solicitudanalisisid),

    # Protocolo
    url(r'^protocolo/$', views.l_protocolo, name="l_protocolo"),
    url(r'^protocolo/alta/$', views.a_protocolo),
    url(r'^protocolo/(?P<id>\d+)/$', views.v_protocolo, name="v_protocolo"),
    url(r'^protocolo/update/(?P<id>\d+)/$', views.u_protocolo),
    url(r'^protocolo/delete/(?P<id>\d+)/$', views.d_protocolo),
    url(r'^j_protocolo/$', views.j_protocolo),
    url(r'^j_protocoloid/(?P<id>\d+)/$', views.j_protocoloid),

    # Individuo Padre
    url(r'^individuopadre/$', views.l_individuopadre, name="l_individuopadre"),
    url(r'^individuopadre/alta/$', views.a_individuopadre),
    url(r'^individuopadre/(?P<id>\d+)/$', views.v_individuopadre, name="v_individuopadre"),
    url(r'^individuopadre/update/(?P<id>\d+)/$', views.u_individuopadre),
    url(r'^individuopadre/delete/(?P<id>\d+)/$', views.d_individuopadre),
    url(r'^j_individuopadre/$', views.j_individuopadre),
    url(r'^j_individuopadreid/(?P<id>\d+)/$', views.j_individuopadreid),

    # Individuos
    url(r'^individuos/$', views.l_individuos, name="l_individuos"),
    url(r'^individuos/alta/$', views.a_individuos),
    url(r'^individuos/(?P<id>\d+)/$', views.v_individuos, name="v_individuos"),
    url(r'^individuos/update/(?P<id>\d+)/$', views.u_individuos),
    url(r'^individuos/delete/(?P<id>\d+)/$', views.d_individuos),
    url(r'^j_individuos/$', views.j_individuos),
    url(r'^j_individuosid/(?P<id>\d+)/$', views.j_individuosid),

    # Detalle Analisis
    url(r'^detalleanalisis/$', views.l_detalleanalisis, name="l_detalleanalisis"),
    url(r'^detalleanalisis/alta/$', views.a_detalleanalisis),
    url(r'^detalleanalisis/(?P<id>\d+)/$', views.v_detalleanalisis, name="v_detalleanalisis"),
    url(r'^detalleanalisis/update/(?P<id>\d+)/$', views.u_detalleanalisis),
    url(r'^detalleanalisis/delete/(?P<id>\d+)/$', views.d_detalleanalisis),
    url(r'^j_detalleanalisis/$', views.j_detalleanalisis),
    url(r'^j_detalleanalisisid/(?P<id>\d+)/$', views.j_detalleanalisisid),

    # eliminacion Protocolo
    url(r'^eliminacionprotocolo/$', views.l_eliminacionprotocolo, name="l_eliminacionprotocolo"),
    url(r'^eliminacionprotocolo/alta/$', views.a_eliminacionprotocolo),
    url(r'^eliminacionprotocolo/(?P<id>\d+)/$', views.v_eliminacionprotocolo, name="v_eliminacionprotocolo"),
    url(r'^eliminacionprotocolo/update/(?P<id>\d+)/$', views.u_eliminacionprotocolo),
    url(r'^eliminacionprotocolo/delete/(?P<id>\d+)/$', views.d_eliminacionprotocolo),
    url(r'^j_eliminacionprotocolo/$', views.j_eliminacionprotocolo),
    url(r'^j_eliminacionprotocoloid/(?P<id>\d+)/$', views.j_eliminacionprotocoloid),

]

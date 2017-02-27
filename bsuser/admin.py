from django.contrib import admin
from bsuser.models import IndividuoPadre, SolicitudAnalisis, Protocolo, Individuos, DetalleAnalisis, EliminacionProtocolo

# Register your models here.

admin.site.register(SolicitudAnalisis)
admin.site.register(Protocolo)
admin.site.register(Individuos)
admin.site.register(DetalleAnalisis)
admin.site.register(EliminacionProtocolo)
admin.site.register(IndividuoPadre)




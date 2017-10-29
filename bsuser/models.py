from django.db import models
from django.core.urlresolvers import reverse 
from bsadmin.models import *

# Create your models here.

class SolicitudAnalisis(models.Model):
	veterinario = models.ForeignKey(Veterinario)
	establecimiento = models.ForeignKey(Establecimiento)
	motivo = models.ForeignKey(Motivos)
	especie = models.ForeignKey(Especie)
	fecha = models.DateField(auto_now=False)
	obs = models.TextField("Observaciones", null=True, blank=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return('%d')%(self.id)

	def get_absolute_url(self):
		return reverse("bsuser:v_solicitudAnalisis", kwargs={"id":self.id})

	

class Protocolo(models.Model):
	numero = models.IntegerField("Numero de Protocolo", unique=True)
	activo = models.BooleanField("Estado Confirmado", default=False)
	
	def __str__(self):
		return('%d')%(self.numero)

	def get_absolute_url(self):
		return reverse("bsuser:v_protocolo", kwargs={"id":self.id})

	
class IndividuoPadre(models.Model):
	identificacion = models.CharField("Identificacion / N° de Caravana", max_length=30)
	raza = models.ForeignKey(Raza)
	def __str__(self):
		return ('%s')%(self.identificacion)

	def get_absolute_url(self):
		return reverse("bsuser:v_individuopadre", kwargs={"id":self.id})

	
class Individuos(models.Model):
	padre = models.ForeignKey(IndividuoPadre)
	nombre = models.CharField("Nombre", max_length=15, null=True, blank=True)
	edad = models.CharField("Edad", max_length=2, null=True, blank=True)
	sexo_choices = (
		('M', 'Macho'),
		('H', 'Hembra'),
		('X', 'NS/NC'),
		)
	sexo = models.CharField("Sexo", max_length=1, choices=sexo_choices, null=True, blank=True, default='X')
	libretasanitaria = models.CharField(max_length=15, null=True, blank=True)
	categoriae = models.ForeignKey(CategoriaE, null=True, blank=True)

	def __str__(self):
		return ('%s')%(self.padre)

	def get_absolute_url(self):
		return reverse("bsuser:v_individuos", kwargs={"id":self.id})

	
class DetalleAnalisisPadre(models.Model):
	solicitud = models.ForeignKey(SolicitudAnalisis)
	protocolo = models.ForeignKey(Protocolo)
	diagnostico = models.ForeignKey(Diagnostico)
	piepagina = models.TextField("Observaciones", null=True, blank=True)
	
	def __str__(self):
		return ('%s, %s, %s')%(self.solicitud, self.protocolo, self.diagnostico)

	def get_absolute_url(self):
		return reverse("bsuser:v_detalleanalisispadre", kwargs={"id":self.id})

class DetalleAnalisis(models.Model):
	#padre = models.ForeignKey(DetalleAnalisisPadre)
	solicitud = models.ForeignKey(SolicitudAnalisis)
	parametros = models.ForeignKey(Parametros, null=False, blank=False)
	individuoPadre = models.ForeignKey(IndividuoPadre)
	valor = models.CharField(max_length=30, null=True, blank=True)

	def __str__(self):
		return ('%s, %s, %s')%(self.individuoPadre, self.parametros, self.valor)

	def get_absolute_url(self):
		return reverse("bsuser:v_detalleanalisis", kwargs={"id":self.id})

class EliminacionProtocolo(models.Model):
	## en vez de Protocolo no debería ser DetalleAnalisisPadre? 
	## '--> no, porque se elimina todo el protocolo, no solo un diagnostico
	#protocolo = models.OneToOneField(Protocolo)
	protocolo = models.ForeignKey(Protocolo)
	fecha = models.DateField(auto_now=False)
	motivoBaja = models.TextField("Motivo de Baja")
	usuario = models.CharField("Responsable", max_length=30) 

	def __str__(self):
		dia = str(self.fecha)
		return('%s, %s')%(self.protocolo, dia)

	def get_absolute_url(self):
		return reverse("bsuser:v_eliminacionprotocolo", kwargs={"id":self.id})

class Tercerizacion(models.Model):
	fecha_envio = models.DateField("Fecha de Envío", auto_now=False)
	fecha_devolucion = models.DateField("Fecha de Devolución", auto_now=False, null=True, blank=True)
	institucion = models.CharField(max_length=20)
	detalleanalisispadre = models.ForeignKey(DetalleAnalisisPadre)
	detalle=models.TextField("Detalle")
	
	def __str__(self):
		return ('%s %s %s')%(self.fecha_envio, self.fecha_devolucion, self.institucion)

	def get_absolute_url(self):
		return reverse("bsuser:v_tercerizar", kwargs={"id": self.id}) #keyword args
		
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

class Protocolo(models.Model):
	numero = models.IntegerField("Numero de Protocolo", unique=True)
	activo = models.BooleanField("Estado Confirmado", default=True)
	
	def __str__(self):
		return('%d')%(self.numero)

class IndividuoPadre(models.Model):
	identificacion = models.CharField("Identificacion / N° de Caravana", max_length=30)
	raza = models.ForeignKey(Raza)
	def __str__(self):
		return ('%s')%(self.identificacion)
	
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


class DetalleAnalisis(models.Model):
	solicitud = models.ForeignKey(SolicitudAnalisis)
	protocolo = models.ForeignKey(Protocolo)
	diagnostico = models.ForeignKey(Diagnostico)
	individuo = models.ForeignKey(Individuos)
	parametros = models.ForeignKey(Parametros)
	valor = models.CharField(max_length=30)

	class Meta:
		unique_together = ('solicitud','protocolo','diagnostico', 'individuo', 'parametros',)


	def __str__(self):
		return ('%s, %s, %s, %s, %s')%(self.solicitud, self.protocolo, self.diagnostico, self.individuo, self.parametros)


class EliminacionProtocolo(models.Model):
	protocolo = models.OneToOneField(Protocolo)
	fecha = models.DateField(auto_now=False)
	motivoBaja = models.TextField("Motivo de Baja")
	#usuario = 

	def __str__(self):
		dia = str(fecha)
		return('%s, %s')%(self.protocolo, self.dia)

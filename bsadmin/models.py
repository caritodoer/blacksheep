from django.db import models
from django.core.urlresolvers import reverse 

# Create your models here.
class Especializacion(models.Model):
	descripcion = models.CharField("Especializacion", max_length=30)

	def __str__(self):
		return ('%s')%(self.descripcion)

	def get_absolute_url(self):
		return reverse("bsadmin:v_especializacion", kwargs={"id":self.id})

class Categoria(models.Model):
	descripcion = models.CharField("Categoria", max_length=30)

	def __str__(self):
		return ('%s')%(self.descripcion)

class Explotacion(models.Model):
	descripcion = models.CharField("Explotacion", max_length=30)

	def __str__(self):
		return ('%s')%(self.descripcion)

class Motivos(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return ('%s')%(self.nombre)


class Especie(models.Model):
	descripcion = models.CharField("Especie", max_length=30)
	
	def __str__(self):
		return ('%s')%(self.descripcion)

class Raza(models.Model):
	nombre = models.CharField(max_length=30)
	especie = models.ForeignKey(Especie)

	def __str__(self):
		return('%s, %s')%(self.nombre, self.especie)

class CategoriaE(models.Model):
	descripcion = models.CharField(max_length=30)
	especie = models.ForeignKey(Especie)

	def __str__(self):
		return ('%s')%(self.descripcion)

class Muestra(models.Model):
	descripcion = models.CharField("Muestra", max_length=30)

	def __str__(self):
		return ('%s')%(self.descripcion)

class Parametros(models.Model):
	descripcion = models.CharField("Parametro", max_length=30)
	tipo_de_dato_choices = (
		('I', 'Entero'),
		('B', 'Positivo/Negativo'),
		('F', 'Numero con decimales'),
		('S', 'Texto'),
		)
	tipo_de_dato = models.CharField("Tipo de Dato", max_length=1, choices=tipo_de_dato_choices)
	unidadmedida = models.CharField("Unidad de Medida",max_length=10)
	grupo = models.CharField(max_length=30, blank=True, null=True)

	def __str__(self):
		return ('%s')%(self.descripcion)

class Diagnostico(models.Model):
	descripcion = models.CharField("Diagnostico", max_length=30)
	## parametros = models.ManyToManyField(Parametros)
	tecnica = models.CharField(max_length=30)
	muestra = models.ForeignKey(Muestra)
	tercerizacion = models.BooleanField()
	activo = models.BooleanField(default=True)
	piepagina = models.TextField("Pie de Pagina", null=True, blank=True)

	def __str__(self):
		return ('%s')%(self.descripcion)

class ValoresReferencia(models.Model):
	diagnostico = models.ForeignKey(Diagnostico)
	especie = models. ForeignKey(Especie)
	parametros = models.ForeignKey(Parametros)
	valorRef = models.CharField(max_length=30, blank=True, null=True)
	valorDef = models.CharField(max_length=30, blank=True, null=True)

	class Meta:
		unique_together = ('diagnostico', 'especie', 'parametros',)

	def __str__(self):
		return ('%s %s %s')%(self.diagnostico, self.especie, self.parametros)

class Veterinario(models.Model):
	nombre = models.CharField("Nombre", max_length=30)
	apellido = models.CharField("Apellido", max_length=30)
	matricula = models.CharField(max_length=10, unique=True)
	dni = models.CharField(max_length=8, unique=True)
	domicilio_particular = models.CharField("Domicilio Particular", max_length=30, blank=True, null=True)
	cp_domicilio_particular = models.CharField("Codigo Postal del Dom.Part.", max_length=4, blank=True, null=True)
	domicilio_fiscal = models.CharField("Domicilio Fiscal", max_length=30)
	cp_domicilio_fiscal = models.CharField("Codigo Postal del Dom.Fisc", max_length=4)
	email = models.EmailField("Email", blank=True, null=True)
	cuit = models.CharField("C.U.I.T.", max_length=13)
	codigo_area = models.CharField("Codigo de Area", max_length=4)
	telefono1 = models.CharField("Telefono 1", max_length=15)
	telefono2 = models.CharField("Telefono 2", max_length=15, blank=True, null=True)
	fecha_ingreso = models.DateField("Fecha de Ingreso", auto_now=False)
	fecha_baja = models.DateField("Fecha de Baja", auto_now=False, null=True, blank=True)
	acreditacion_brucelosis = models.CharField("Numero de Acreditacion de Brucelosis", max_length=15, null=True, blank=True)
	acreditacion_aie = models.CharField("Numero de Acreditacion de A.I.E.", max_length=15, null=True, blank=True)
	especializaciones = models.ManyToManyField(Especializacion)
	activo = models.BooleanField(default=True, blank=True)

	def __str__(self):
		return ('%s, %s')%(self.apellido, self.nombre)

	def get_absolute_url(self):
		return reverse("alpha:detalle", kwargs={"id": self.id}) #keyword args

class Establecimiento(models.Model):
	nombre = models.CharField(max_length=50)
	partido = models.CharField(max_length=20)
	propietario = models.CharField(max_length=30)
	RENSPA = models.CharField(max_length=30)
	CUIT = models.CharField(max_length=30, null=True, blank=True)
	veterinario = models.ForeignKey(Veterinario, verbose_name="Veterinario de Cabecera")
	categorias = models.ManyToManyField(Categoria)
	explotacion = models.ManyToManyField(Explotacion)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return ('%s %s')%(self.nombre, self.partido)


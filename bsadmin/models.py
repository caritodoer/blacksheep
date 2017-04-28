from django.db import models
from django.core.urlresolvers import reverse 

# Create your models here.
class Especializacion(models.Model):
	descripcion = models.CharField("Especializacion", max_length=30, unique=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return ('%s')%(self.descripcion)

	def get_absolute_url(self):
		return reverse("bsadmin:v_especializacion", kwargs={"id":self.id})

	def save(self, force_insert=False, force_update=False):
		self.descripcion=self.descripcion.upper()
		super(Especializacion, self).save(force_insert, force_update)

class Categoria(models.Model):
	descripcion = models.CharField("Categoria", max_length=30, unique=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return ('%s')%(self.descripcion)

	def get_absolute_url(self):
		return reverse("bsadmin:v_categoria", kwargs={"id":self.id})

	def save(self, force_insert=False, force_update=False):
		self.descripcion=self.descripcion.upper()
		super(Categoria, self).save(force_insert, force_update)

class Explotacion(models.Model):
	descripcion = models.CharField("Explotacion", max_length=30, unique=True)
	activo = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse("bsadmin:v_explotacion",kwargs={"id":self.id})
	def __str__(self):
		return ('%s')%(self.descripcion)
	def save(self,force_insert=False,force_update=False):
		self.descripcion=self.descripcion.upper()
		super(Explotacion,self).save(force_insert,force_update)

class Motivos(models.Model):
	descripcion = models.CharField("Motivos", max_length=30, unique=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return ('%s')%(self.descripcion)

	def get_absolute_url(self):
		return reverse("bsadmin:v_motivos", kwargs={"id": self.id})

	def save(self, force_insert=False, force_update=False):
		self.descripcion = self.descripcion.upper()
		super(Motivos, self).save(force_insert, force_update)


class Especie(models.Model):
	descripcion = models.CharField("Especie", max_length=30, unique=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return ('%s')%(self.descripcion)

	def get_absolute_url(self):
		return reverse("bsadmin:v_especie", kwargs={"id":self.id})

	def save(self, force_insert=False, force_update=False):
		self.descripcion = self.descripcion.upper()
		super(Motivos, self).save(force_insert, force_update)

class Raza(models.Model):
	descripcion = models.CharField(max_length=30, unique=True)
	especie = models.ForeignKey(Especie)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return('%s, %s')%(self.descripcion, self.especie)

	def get_absolute_url(self):
		return reverse("bsadmin:v_raza", kwargs={"id": self.id})

	def save(self, force_insert=False, force_update=False):
		self.descripcion = self.descripcion.upper()
		super(Raza, self).save(force_insert, force_update)

class CategoriaE(models.Model):
	descripcion = models.CharField(max_length=30, unique=True)
	especie = models.ForeignKey(Especie)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return ('%s')%(self.descripcion)

	def get_absolute_url(self):
		return reverse("bsadmin:v_categoriae", kwargs={"id": self.id})

	def save(self, force_insert=False, force_update=False):
		self.descripcion = self.descripcion.upper()
		super(CategoriaE, self).save(force_insert, force_update)


class Muestra(models.Model):
	descripcion = models.CharField("Muestra", max_length=30, unique=True)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return ('%s')%(self.descripcion)

	def get_absolute_url(self):
		return reverse("bsadmin:v_muestra", kwargs={"id": self.id})

	def save(self, force_insert=False, force_update=False):
		self.descripcion = self.descripcion.upper()
		super(Muestra, self).save(force_insert, force_update)

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
	activo = models.BooleanField(default=True)

	def __str__(self):
		return ('%s, %s')%(self.descripcion, self.grupo)

	def get_absolute_url(self):
		return reverse("bsadmin:v_parametros", kwargs={"id": self.id})

	def save(self, force_insert=False, force_update=False):
		self.descripcion = self.descripcion.upper()
		self.grupo = self.grupo.upper()
		super(Parametros, self).save(force_insert, force_update)


class Diagnostico(models.Model):
	descripcion = models.CharField("Diagnostico", max_length=30)
	## esta comentado porque ValoresReferencia es el vinculo entre Diagnostico y Parametros
	## parametros = models.ManyToManyField(Parametros) 
	tecnica = models.CharField(max_length=30)
	muestra = models.ForeignKey(Muestra)
	tercerizacion = models.BooleanField()
	activo = models.BooleanField(default=True)
	piepagina = models.TextField("Pie de Pagina", null=True, blank=True)

	def __str__(self):
		return ('%s')%(self.descripcion)
	def get_absolute_url(self):
		return reverse("bsadmin:v_diagnostico", kwargs={"id": self.id})

	def save(self, force_insert=False, force_update=False):
		self.descripcion = self.descripcion.upper()
		self.tecnica = self.tecnica.upper()
		super(Diagnostico, self).save(force_insert, force_update)

class ValoresReferencia(models.Model):
	diagnostico = models.ForeignKey(Diagnostico)
	especie = models. ForeignKey(Especie)
	parametros = models.ForeignKey(Parametros)
	valorRef = models.CharField(max_length=30, blank=True, null=True)
	valorDef = models.CharField(max_length=30, blank=True, null=True)
	activo = models.BooleanField(default=True)

	class Meta:
		unique_together = ('diagnostico', 'especie', 'parametros',)

	def __str__(self):
		return ('%s %s %s')%(self.diagnostico, self.especie, self.parametros)

	def get_absolute_url(self):
		return reverse("bsadmin:v_valoresreferencia", kwargs={"id": self.id})

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
		return reverse("bsadmin:v_veterinario", kwargs={"id": self.id}) #keyword args


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

	def get_absolute_url(self):
		return reverse("bsadmin:v_establecimiento", kwargs={"id": self.id}) #keyword args


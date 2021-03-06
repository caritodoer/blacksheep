from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.colors import pink, green, brown, white, black, magenta, red
import time
from reportlab.lib.enums import *
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, TableStyle, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
from bsadmin.models import *
from .models import *
from django.views.generic import ListView
from reportlab.lib.utils import ImageReader

PAGE_HEIGHT=A4[1]
PAGE_WIDTH=A4[0]
styles = getSampleStyleSheet()

pdfmetrics.registerFont(TTFont('Existence-Light', '../blacksheep/static/fonts/Existence-Light.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-B', '../blacksheep/static/fonts/ubuntu-font-family-0.83/Ubuntu-B.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-L', '../blacksheep/static/fonts/ubuntu-font-family-0.83/Ubuntu-L.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-M', '../blacksheep/static/fonts/ubuntu-font-family-0.83/Ubuntu-M.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-C', '../blacksheep/static/fonts/ubuntu-font-family-0.83/Ubuntu-C.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-R', '../blacksheep/static/fonts/ubuntu-font-family-0.83/Ubuntu-R.ttf'))

styles.add(ParagraphStyle(name='tit2', alignment=TA_CENTER, fontName = "Ubuntu-M", fontSize = 14))
styles.add(ParagraphStyle(name='tit1', alignment=TA_CENTER, fontName = "Existence-Light", fontSize = 16))
styles.add(ParagraphStyle(name='tit3', alignment=TA_LEFT, fontName = "Ubuntu-L", fontSize = 12))
styles.add(ParagraphStyle(name='tablas', alignment=TA_LEFT, fontName = "Ubuntu-C", fontSize = 11))
styles.add(ParagraphStyle(name='textos', alignment=TA_LEFT, fontName = "Ubuntu-R", fontSize = 10))

tit1 = styles["tit1"]
tit2 = styles["tit2"]
tit3 = styles["tit3"]
tablas = styles["tablas"]
textos = styles["textos"]

LIST_STYLE = TableStyle(
	[('GRID', (0,0), (10, -1), 1, colors.lightblue),
	('BACKGROUND', (0,0), (-1, 0), colors.lightblue),
	('FONT', (0,0), (-1, -1), 'Ubuntu-C', 10)]
)


def encabezado(canvas):
	#
	# Datos de la empresa
	#
	empresa = Empresa.objects.all()
	if empresa:
		for e in empresa:
			nombre = e.nombre
			subtitulo = e.subtitulo
			direccion = e.direccion
			ciudad = e.ciudad
			telefono = e.telefono
			email = e.email
			logo = ImageReader(e.logo.path)

		canvas.saveState()
		canvas.drawImage(logo, 0.75*inch, PAGE_HEIGHT - 70, width=0.75*inch, height=0.75*inch, mask='auto')

		canvas.setFont('Existence-Light', 18)
		canvas.drawString(1.60*inch, PAGE_HEIGHT - 40, nombre)
		canvas.setFont('Existence-Light', 16)
		canvas.drawString(1.60*inch, PAGE_HEIGHT - 60, subtitulo)
		contacto_parts = [direccion, ciudad, telefono, email]
		canvas.setFont("Ubuntu-M", 9)
		y=PAGE_HEIGHT-35
		for part in contacto_parts:
			canvas.drawRightString (PAGE_WIDTH - 0.75*inch, y, part)
			y=y-10
		canvas.setLineWidth(1.0) 
		canvas.line (0.70*inch, PAGE_HEIGHT-75 , PAGE_WIDTH-50, PAGE_HEIGHT-75) #horizontal
		canvas.restoreState()
def solicitud(canvas, instance_dap, title):
	canvas.saveState()
	canvas.setFont('Ubuntu-M', 16)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-100, title)

	canvas.setFont("Ubuntu-R", 9)
	establ= instance_dap.solicitud.establecimiento
	prop=instance_dap.solicitud.establecimiento.propietario
	renspa= instance_dap.solicitud.establecimiento.RENSPA
	vet= instance_dap.solicitud.veterinario
	obs=instance_dap.solicitud.obs
	solicitud_parts  = ["Establecimiento: %s" %(establ), "Propietario: %s" %(prop), "R.E.N.S.P.A.: %s" %(renspa), "Veterinario: %s" %(vet), "Observaciones: %s" %(obs)]
	y=PAGE_HEIGHT-130
	for part in solicitud_parts:
		canvas.drawString (0.75*inch, y, part)
		y=y-10

	fecha=instance_dap.solicitud.fecha
	motivo= instance_dap.solicitud.motivo
	protocolo=instance_dap.protocolo
	solicitud_parts  = ["Fecha Recepción: %s" %(fecha), "Motivo: %s" %(motivo), "N° de Protocolo: %s" %(protocolo)]
	# canvas.setFont("Helvetica", 9)
	y=PAGE_HEIGHT-130
	for part in solicitud_parts:
		canvas.drawString (PAGE_WIDTH/2.0, y, part)
		y=y-10

	canvas.restoreState()
def primeraPagina(canvas, doc, instance_dap, title):
	piepagina=instance_dap.diagnostico.piepagina
	#
	# Datos de la empresa
	#
	empresa = Empresa.objects.all()
	if empresa:
		for e in empresa:
			nombre = e.nombre
			subtitulo = e.subtitulo
			direccion = e.direccion
			ciudad = e.ciudad
			telefono = e.telefono
			email = e.email
			logo = ImageReader(e.logo.path)
		encabezado(canvas)
		solicitud(canvas, instance_dap, title)
		canvas.saveState()
		# numeracion de pagina
		canvas.setFont('Ubuntu-R', 8)
		canvas.drawString(inch, 1.00 * inch, "%s" %(piepagina))
		canvas.drawString(inch, 0.75 * inch, "Primera pagina / %s %s" %(nombre, subtitulo))
		canvas.restoreState()
def myLaterPages(canvas, doc, instance_dap, title):
	#
	# Datos de la empresa
	#
	empresa = Empresa.objects.all()
	if empresa:
		for e in empresa:
			nombre = e.nombre
			subtitulo = e.subtitulo
			direccion = e.direccion
			ciudad = e.ciudad
			telefono = e.telefono
			email = e.email
			logo = ImageReader(e.logo.path)
		canvas.saveState()
		encabezado(canvas)
		solicitud(canvas, instance_dap, title)
		
		# numeracion de pagina
		canvas.setFont('Ubuntu-R', 8)
		canvas.drawString(inch, 0.75 * inch, "Página %d / %s %s" %(doc.page, nombre, subtitulo))
		canvas.restoreState()

def informe(request, id=None):
	print("entra al informe")
	#pedidos a BDD
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	piepagina_dap=instance.piepagina
	
	diag = instance.diagnostico
	all_param_del_diag = Parametros.objects.all().filter(diagnostico=diag)
	solic = instance.solicitud
	all_indiv_de_solic = DetalleAnalisis.objects.distinct('individuoPadre').filter(solicitud=solic)
	grupo_list_t = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="T")
	grupo_list_i = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="I")
	grupo_gral = Parametros.objects.distinct('grupo').filter(diagnostico=diag)
	# trae un unico individuo para la parte del listar los ítmes una sola vez en el HTML	
	cant_indi = len(all_indiv_de_solic)
	indi = all_indiv_de_solic[cant_indi-1]

	# listado de valores de referencia filtrado por diag + param + especie
	vdr_all = ValoresReferencia.objects.all()
	vdr_list=[]
	for v in vdr_all:
		for p in all_param_del_diag:
			if v.parametros == p:
				if v.especie == instance.solicitud.especie:
					vdr_list.append(v)
	print("vdr_list")
	print(vdr_list)
	da_all = DetalleAnalisis.objects.all().filter(solicitud=solic)
	da_list = {}
	valor=""
	for p in all_param_del_diag:
		for i in all_indiv_de_solic:
			for da in da_all:
				ban1=0
				if da.parametros == p:
					if da.individuoPadre == i.individuoPadre:
						if da.valor != '':
							print("entro 1")
							valor=da.valor
							#print(linea)
							ban1=1
						else:
							for vdr in vdr_list:
								if vdr.parametros == p:
									print("entro 2")
									valor=vdr.valorDef
									ban1=1
							if ban1==0:
								print("entro 3")
								valor=""
								ban1=1
						da_list[da]=valor
	# print("da_list")
	# print(da_list)


	grupos = {}
	for g in grupo_list_t:
		cant=0
		for p in all_param_del_diag:
			if g.grupo == p.grupo:
				cant=cant+1
		inicio=0
		fin=5
		k=g.grupo
		list_r=[]
		ban=True
		while ban:
			rango= Parametros.objects.all().filter(diagnostico=diag, visualizacion1="T", grupo=k)[inicio:fin]
			#print("g rango  ", rango)
			list_r.append(rango)
			if fin < cant:
				ban=True
				inicio = inicio+5
				fin = fin+5
			else:
				ban=False
		grupos[k] = list_r
	
	#info basica pars generar pdf
	response = HttpResponse(content_type='application/pdf')
	pdf_name = "informe_%s.pdf" %instance.diagnostico
	response['Content-Disposition'] = 'filename=%s; pagesize=A4' %pdf_name
	buff = BytesIO()
	title = "Informe de Resultados"
	# constante p/ 1ra pagina
	def myFirstPage(canvas, doc):
		primeraPagina(canvas, doc, instance, title)

	def pagSiguientes(canvas, doc):
		myLaterPages(canvas, doc, instance, title)

	# cuerpo
	def cuerpo(canvas):
		#Iniciamos el story para los registros
		Story = [Spacer(1, 100)]
		
		title = instance.diagnostico.descripcion
		p = Paragraph(title, tit2)
		Story.append(p)
		Story.append(Spacer(1, 12))

		subtitle = instance.diagnostico.tecnica
		p = Paragraph("Tecnica: "+subtitle, tit3)
		Story.append(p)
		Story.append(Spacer(1, 12))
		
		#Definimos un estilo
		style = styles["textos"]
		Story.append(Spacer(1, 12))

		for key, value in grupos.items():
			for v in value:
				header = Paragraph(key, tit3)
				Story.append(header)
				Story.append(Spacer(1, 20))
				headings = ["#ID", ]
				for p in v:
					headings.append(p.descripcion)
					# headings.append("u.")
				allregistros = []
				for i in all_indiv_de_solic:
					registros=[]
					registros.append(i.individuoPadre.identificacion)
					for p in v:
						for da, valor in da_list.items():
							if i.individuoPadre.identificacion == da.individuoPadre.identificacion and p == da.parametros:
								reg = valor + " " + p.unidadmedida
								registros.append(reg)
					allregistros.append(registros)
					#print(allregistros)
				t = Table([headings] + allregistros)
				t.setStyle(LIST_STYLE)
				# print(len(headings))
				t._argW[0]=1*inch
				for i in range (1,len(headings)):
					t._argW[i]=1.3*inch
				# t._argW[3]=5.5*inch
				Story.append(t)
				Story.append(Spacer(1, 12))
		
		for g in grupo_list_i:
			header=Paragraph(g.grupo, tit3)
			Story.append(header)
			Story.append(Spacer(1, 12))

			for da in da_all:
				if g.grupo == da.parametros.grupo and da.individuoPadre == indi.individuoPadre:
					par_val=" - "+da.parametros.descripcion+": "+da.valor
					item_p = Paragraph(par_val, textos)
					Story.append(item_p)

							# ban2=0

							# for vdr in vdr_list:
							# 	if  vdr.parametros == p:
							# 		vdr_valor = " - Valor de Referencia: "+vdr.valorRef
							# 		ban2=1
							# if ban2 == 0:
							# 	item_p = Paragraph(par_val, textos)
							# 	Story.append(item_p)
							# else:	
							# 	item_p = Paragraph(par_val+vdr_valor, textos)
							# 	Story.append(item_p)
								

		
		Story.append(Spacer(1, 20))
		if piepagina_dap:
			pie_dap = Paragraph("Observaciones: ", tit3)
			Story.append(pie_dap)
			Story.append(Spacer(1, 12))
			pie_dap = Paragraph(piepagina_dap, textos)
			Story.append(pie_dap)
			Story.append(Spacer(1, 12))
		
		# poner en pagina aparte
		Story.append(PageBreak())
		Story.append(Spacer(1, 100))
		title = "Valores de Referencia"
		p = Paragraph(title, tit2)
		Story.append(p)
		Story.append(Spacer(1, 20))

		for g in grupo_gral:
			print(g.grupo)
			#grupo_nombre = g.grupo
			grupo_nombre = Paragraph(g.grupo, tit3)
			Story.append(grupo_nombre)
			Story.append(Spacer(1, 10))
			for valor in vdr_all:
				if valor.parametros.grupo == g.grupo:
					#print(valor.parametros.descripcion+": "+valor.valorRef)
					param_vRef = " - "+valor.parametros.descripcion+": "+valor.valorRef
					item = Paragraph(param_vRef, textos)
					Story.append(item)
			Story.append(Spacer(1, 10))

		return Story

	
	# cierre Story	
	Story = cuerpo(canvas)
	#Creamos un documento basándonos en una plantilla
	doc = SimpleDocTemplate(buff, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=75)
	#Construimos el documento a partir de los argumentos definidos
	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=pagSiguientes)
	response.write(buff.getvalue())
	buff.close()
	return response
def general(request, id=None):
	print("entra al informe")
	#info basica pars generar pdf
	response = HttpResponse(content_type='application/pdf')
	pdf_name = "informe_general.pdf"
	response['Content-Disposition'] = 'filename=%s; pagesize=A4' %pdf_name
	buff = BytesIO()
	title = "Informe General"

	#pedidos a BDD
	dap_inicial = get_object_or_404(DetalleAnalisisPadre, id=id)
	diag_x_prot = DetalleAnalisisPadre.objects.all().filter(protocolo=dap_inicial.protocolo)
	# constante p/ 1ra pagina
	def myFirstPage(canvas, doc):
		primeraPagina(canvas, doc, dap_inicial, title)

	def pagSiguientes(canvas, doc):
		myLaterPages(canvas, doc, dap_inicial, title)
	

	# cuerpo
	def cuerpo(canvas):
		Story = [Spacer(1, 1)]
		for instance in diag_x_prot:
			Story.append(Spacer(1, 100))
			ter = Tercerizacion.objects.all().filter(detalleanalisispadre=instance)
			if instance.diagnostico.tercerizacion or ter:
				if dap_inicial.diagnostico.tercerizacion:
					print("Tercerizado1")
					title = instance.diagnostico.descripcion
					p = Paragraph(title, tit2)
					Story.append(p)
					Story.append(Spacer(1, 12))

					subtitle = instance.diagnostico.tecnica
					p = Paragraph("Tecnica: "+subtitle, tit3)
					Story.append(p)
					Story.append(Spacer(1, 12))

					detalle = "Este Diagnostico es tercerizado"
					p = Paragraph(detalle, tit3)
					Story.append(p)
					Story.append(Spacer(1, 12))

				if ter:
					print("Tercerizado2")
					title = instance.diagnostico.descripcion
				
					p = Paragraph(title, tit2)
					Story.append(p)
					Story.append(Spacer(1, 12))
					detalle = "Este Diagnostico fue tercerizado."
					p = Paragraph(detalle, tit3)
					Story.append(p)
					Story.append(Spacer(1, 12))
				
					style = styles["textos"]
					for t in ter:
						f_e=str(t.fecha_envio)
						print(f_e)
						print(type(f_e))
						fecha_envio = Paragraph("Fecha de Envío: "+f_e, style) 
						Story.append(fecha_envio)
						Story.append(Spacer(1, 12))
						if t.fecha_devolucion:
							f_d=str(t.fecha_devolucion)
							fecha_devolucion = Paragraph("Fecha de Devolución: "+f_d, style)
							Story.append(fecha_devolucion)
							Story.append(Spacer(1, 12))
						institucion = Paragraph("Institución: "+t.institucion, style) 
						Story.append(institucion)
						Story.append(Spacer(1, 12))
						detalle = Paragraph("Detalle:", tit3) 
						Story.append(detalle)
						Story.append(Spacer(1, 12))
						detalle = Paragraph(t.detalle, style) 
						Story.append(detalle)
						Story.append(Spacer(1, 12))
			else:
				#Iniciamos el story para los registros
				title = instance.diagnostico.descripcion
				
				p = Paragraph(title, tit2)
				Story.append(p)
				Story.append(Spacer(1, 12))
				
				#Definimos un estilo
				style = styles["textos"]
				Story.append(Spacer(1, 12))

				piepagina_dap=instance.piepagina
				diag = instance.diagnostico
				all_param_del_diag = Parametros.objects.all().filter(diagnostico=diag)
				solic = instance.solicitud
				all_indiv_de_solic = DetalleAnalisis.objects.distinct('individuoPadre').filter(solicitud=solic)
				grupo_list_t = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="T")
				grupo_list_i = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="I")
				grupo_gral = Parametros.objects.distinct('grupo').filter(diagnostico=diag)
				# trae un unico individuo para la parte del listar los ítmes una sola vez en el HTML	
				cant_indi = len(all_indiv_de_solic)
				indi = all_indiv_de_solic[cant_indi-1]

				# listado de valores de referencia filtrado por diag + param + especie
				vdr_all = ValoresReferencia.objects.all()
				vdr_list=[]
				for v in vdr_all:
					for p in all_param_del_diag:
						if v.parametros == p:
							if v.especie == instance.solicitud.especie:
								vdr_list.append(v)
				#print("vdr_list")
				#print(vdr_list)
				da_all = DetalleAnalisis.objects.all().filter(solicitud=solic)
				da_list = {}
				valor=""
				for p in all_param_del_diag:
					for i in all_indiv_de_solic:
						for da in da_all:
							ban1=0
							if da.parametros == p:
								if da.individuoPadre == i.individuoPadre:
									if da.valor != '':
										print("entro 1")
										valor=da.valor
										#print(linea)
										ban1=1
									else:
										for vdr in vdr_list:
											if vdr.parametros == p:
												print("entro 2")
												valor=vdr.valorDef
												ban1=1
										if ban1==0:
											print("entro 3")
											valor=""
											ban1=1
								da_list[da]=valor
				# print("da_list")
				# print(da_list)


				grupos = {}
				for g in grupo_list_t:
					cant=0
					for p in all_param_del_diag:
						if g.grupo == p.grupo:
							cant=cant+1
					inicio=0
					fin=5
					k=g.grupo
					list_r=[]
					ban=True
					while ban:
						rango= Parametros.objects.all().filter(diagnostico=diag, visualizacion1="T", grupo=k)[inicio:fin]
						#print("g rango  ", rango)
						list_r.append(rango)
						if fin < cant:
							ban=True
							inicio = inicio+5
							fin = fin+5
						else:
							ban=False
					grupos[k] = list_r
			
	
	

				for key, value in grupos.items():
					for v in value:
						header = Paragraph(key, tit3)
						Story.append(header)
						Story.append(Spacer(1, 20))
						headings = ["#ID", ]
						for p in v:
							headings.append(p.descripcion)
							# headings.append("u.")
						allregistros = []
						for i in all_indiv_de_solic:
							registros=[]
							registros.append(i.individuoPadre.identificacion)
							for p in v:
								for da, valor in da_list.items():
									if i.individuoPadre.identificacion == da.individuoPadre.identificacion and p == da.parametros:
										reg = valor + " " + p.unidadmedida
										registros.append(reg)
							allregistros.append(registros)
							#print(allregistros)
						t = Table([headings] + allregistros)
						t.setStyle(LIST_STYLE)
						# print(len(headings))
						t._argW[0]=1*inch
						for i in range (1,len(headings)):
							t._argW[i]=1.3*inch
						# t._argW[3]=5.5*inch
						Story.append(t)
						Story.append(Spacer(1, 12))
				
				for g in grupo_list_i:
					header=Paragraph(g.grupo, tit3)
					Story.append(header)
					Story.append(Spacer(1, 12))

					for da in da_all:
						if g.grupo == da.parametros.grupo and da.individuoPadre == indi.individuoPadre:
							par_val=" - "+da.parametros.descripcion+": "+da.valor
							item_p = Paragraph(par_val, textos)
							Story.append(item_p)

		
				Story.append(Spacer(1, 20))
				if piepagina_dap:
					pie_dap = Paragraph("Observaciones: ", tit3)
					Story.append(pie_dap)
					Story.append(Spacer(1, 12))
					pie_dap = Paragraph(piepagina_dap, textos)
					Story.append(pie_dap)
					Story.append(Spacer(1, 12))
				
				# poner en pagina aparte
				Story.append(PageBreak())
				Story.append(Spacer(1, 100))
				title = "Valores de Referencia"
				p = Paragraph(title, tit2)
				Story.append(p)
				Story.append(Spacer(1, 20))

				for g in grupo_gral:
					print(g.grupo)
					#grupo_nombre = g.grupo
					grupo_nombre = Paragraph(g.grupo, tit3)
					Story.append(grupo_nombre)
					Story.append(Spacer(1, 10))
					for valor in vdr_all:
						if valor.parametros.grupo == g.grupo:
							#print(valor.parametros.descripcion+": "+valor.valorRef)
							param_vRef = " - "+valor.parametros.descripcion+": "+valor.valorRef
							item = Paragraph(param_vRef, textos)
							Story.append(item)
					Story.append(Spacer(1, 10))

			Story.append(PageBreak())

		return Story

	
	# cierre Story	
	Story = cuerpo(canvas)
	#Creamos un documento basándonos en una plantilla
	doc = SimpleDocTemplate(buff, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=75)
	#Construimos el documento a partir de los argumentos definidos
	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=pagSiguientes)
	response.write(buff.getvalue())
	buff.close()
	return response
	

	
def hojadetrabajo(request, id=None):
	# Hacemos los pedidos a BDD que necesitamos
	instance = get_object_or_404(DetalleAnalisisPadre, id=id)
	diag = instance.diagnostico
	all_param_del_diag = Parametros.objects.all().filter(diagnostico=diag)
	solic = instance.solicitud
	all_indiv_de_solic = DetalleAnalisis.objects.distinct('individuoPadre').filter(solicitud=solic)
	grupo_list_t = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="T")
	grupo_list_i = Parametros.objects.distinct('grupo').filter(diagnostico=diag, visualizacion1="I")
	grupos = {}
	for g in grupo_list_t:
		cant=0
		for p in all_param_del_diag:
			if g.grupo == p.grupo:
				cant=cant+1
		inicio=0
		fin=5
		k=g.grupo
		list_r=[]
		ban=True
		while ban:
			rango= Parametros.objects.all().filter(diagnostico=diag, visualizacion1="T", grupo=k)[inicio:fin]
			#print("g rango  ", rango)
			list_r.append(rango)
			if fin < cant:
				ban=True
				inicio = inicio+5
				fin = fin+5
			else:
				ban=False
		grupos[k] = list_r
	
	response = HttpResponse(content_type='application/pdf')
	pdf_name = "hojadetrabajo_%s.pdf" %instance.diagnostico
	response['Content-Disposition'] = 'filename=%s; pagesize=A4' %pdf_name
	buff = BytesIO()
	title = "Hoja de Trabajo"
	
	def myFirstPage(canvas, doc):
		primeraPagina(canvas, doc, instance, title)

	def pagSiguientes(canvas, doc):
		myLaterPages(canvas, doc, instance, title)

	def cuerpo(canvas):
		#Iniciamos el story para los registros
		Story = [Spacer(1, 100)]
		title = instance.diagnostico.descripcion
		
		p = Paragraph(title, tit2)
		Story.append(p)
		Story.append(Spacer(1, 12))

		subtitle = instance.diagnostico.tecnica
		p = Paragraph("Tecnica: "+subtitle, tit3)
		Story.append(p)
		Story.append(Spacer(1, 12))
		
		#Definimos un estilo
		style = styles["textos"]
		Story.append(Spacer(1, 12))

		for key, value in grupos.items():
			for v in value:
				header = Paragraph(key, tit3)
				Story.append(header)
				Story.append(Spacer(1, 20))
				headings = ["#Id", ]
				for p in v:
					headings.append(p.descripcion)
					# headings.append("u.")
				allregistros = []
				for i in all_indiv_de_solic:
					registros=[]
					registros.append(i.individuoPadre.identificacion)
					for p in v:
						registros.append("")
					allregistros.append(registros)
					#print(allregistros)
				t = Table([headings] + allregistros)
				t.setStyle(LIST_STYLE)
				# print(len(headings))
				t._argW[0]=1*inch
				for i in range (1,len(headings)):
					t._argW[i]=1.3*inch
				# t._argW[3]=5.5*inch
				Story.append(t)
				Story.append(Spacer(1, 12))
		
		for g in grupo_list_i:
			header=Paragraph(g.grupo, tit3)
			Story.append(header)
			Story.append(Spacer(1, 12))

			for p in all_param_del_diag:
				if g.grupo == p.grupo:
					item_p = Paragraph(p.descripcion+": ____________________", style) 
					Story.append(item_p)

		Story.append(Spacer(1, 12))

		Story.append(Spacer(1, 20))
	
		pie_dap = Paragraph("Observaciones: ", tit3)
		Story.append(pie_dap)
		Story.append(Spacer(1, 12))
		pie_dap = Paragraph("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________", textos)
		Story.append(pie_dap)
		Story.append(Spacer(1, 12))
		return Story

	Story = cuerpo(canvas)
	#Creamos un documento basándonos en una plantilla
	doc = SimpleDocTemplate(buff, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=75)
	#Construimos el documento a partir de los argumentos definidos
	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=pagSiguientes)
	response.write(buff.getvalue())
	buff.close()
	return response
def tercerizar(request, id=None):
	instance_dap = get_object_or_404(DetalleAnalisisPadre, id=id)
	ter = Tercerizacion.objects.all().filter(detalleanalisispadre=instance_dap)
	response = HttpResponse(content_type='application/pdf')
	pdf_name = "tercerizacion_%s.pdf" %instance_dap.protocolo
	response['Content-Disposition'] = 'filename=%s; pagesize=A4' %pdf_name
	buff = BytesIO()
	title = "Tercerizacion de Protocolo N°%d" %instance_dap.protocolo.numero

	def myFirstPage(canvas, doc):
		primeraPagina(canvas, doc, instance_dap, title)

	def pagSiguientes(canvas, doc):
		myLaterPages(canvas, doc, instance_dap, title)

	def cuerpo(canvas):
		Story = [Spacer(1, 150)]
		style = styles["textos"]
		print(ter)
		for t in ter:
			f_e=str(t.fecha_envio)
			print(f_e)
			print(type(f_e))
			fecha_envio = Paragraph("Fecha de Envío: "+f_e, style) 
			Story.append(fecha_envio)
			Story.append(Spacer(1, 12))
			if t.fecha_devolucion:
				f_d=str(t.fecha_devolucion)
				fecha_devolucion = Paragraph("Fecha de Devolución: "+f_d, style)
				Story.append(fecha_devolucion)
				Story.append(Spacer(1, 12))
			institucion = Paragraph("Institución: "+t.institucion, style) 
			Story.append(institucion)
			Story.append(Spacer(1, 12))
			detalle = Paragraph("Detalle:", tit3) 
			Story.append(detalle)
			Story.append(Spacer(1, 12))
			detalle = Paragraph(t.detalle, style) 
			Story.append(detalle)
			Story.append(Spacer(1, 12))

		return Story

	Story = cuerpo(canvas)
	#Creamos un documento basándonos en una plantilla
	doc = SimpleDocTemplate(buff, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=75)
	#Construimos el documento a partir de los argumentos definidos
	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=pagSiguientes)
	response.write(buff.getvalue())
	buff.close()
	return response
def eliminacionprotocolo(request, id=None):
	instance = get_object_or_404(EliminacionProtocolo, id=id)
	query_dap = DetalleAnalisisPadre.objects.distinct('solicitud').filter(protocolo=instance.protocolo)
	print(query_dap)
	for i in query_dap:
		dap = i.id
		print(i.id)
	
	instance_dap = get_object_or_404(DetalleAnalisisPadre, id=dap)
	response = HttpResponse(content_type='application/pdf')
	pdf_name = "eliminacion_protocolo_%s.pdf" %instance.protocolo
	response['Content-Disposition'] = 'filename=%s; pagesize=A4' %pdf_name
	buff = BytesIO()
	title = "Eliminación de Protocolo N°%d" %instance.protocolo.numero

	def myFirstPage(canvas, doc):
		primeraPagina(canvas, doc, instance_dap, title)

	def pagSiguientes(canvas, doc):
		myLaterPages(canvas, doc, instance_dap, title)

	def cuerpo(canvas):
		Story = [Spacer(1, 150)]
		style = styles["textos"]
		f=str(instance.fecha)
		fecha = Paragraph("Fecha de Baja: "+f, style) 
		Story.append(fecha)
		Story.append(Spacer(1, 12))
		usuario = Paragraph("Responsable: "+instance.usuario, style) 
		Story.append(usuario)
		Story.append(Spacer(1, 12))
		motivoBaja = Paragraph("Motivo de Baja: ", tit3) 
		Story.append(motivoBaja)
		Story.append(Spacer(1, 12))
		motivoBaja = Paragraph(instance.motivoBaja, style) 
		Story.append(motivoBaja)
		Story.append(Spacer(1, 12))

		return Story

	Story = cuerpo(canvas)
	#Creamos un documento basándonos en una plantilla
	doc = SimpleDocTemplate(buff, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=75)
	#Construimos el documento a partir de los argumentos definidos
	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=pagSiguientes)
	response.write(buff.getvalue())
	buff.close()
	return response

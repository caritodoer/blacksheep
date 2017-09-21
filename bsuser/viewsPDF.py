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

PAGE_HEIGHT=A4[1]
PAGE_WIDTH=A4[0]
styles = getSampleStyleSheet()

pdfmetrics.registerFont(TTFont('Existence-Light', '../blacksheep/static/fonts/Existence-Light.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-B', '../blacksheep/static/fonts/ubuntu-font-family-0.83/Ubuntu-B.ttf'))
pdfmetrics.registerFont(TTFont('Ubuntu-M', '../blacksheep/static/fonts/ubuntu-font-family-0.83/Ubuntu-M.ttf'))
styles.add(ParagraphStyle(name='tit2', alignment=TA_CENTER, fontName = "Ubuntu-B",
			fontSize = 14))
tit2 = styles["tit2"]

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
			if fin <= cant:
				ban=True
				inicio = inicio+5
				fin = fin+5
			else:
				ban=False
		grupos[k] = list_r
	
	# Aca comienza la configuracion del PDF
	response = HttpResponse(content_type='application/pdf')
	pdf_name = "hojadetrabajo_%s.pdf" %instance.diagnostico
	response['Content-Disposition'] = 'filename=%s; pagesize=A4' %pdf_name

	buff = BytesIO()
	
	def encabezado(canvas):
		canvas.saveState()
		canvas.setFont('Existence-Light', 22)
		canvas.drawString(0.75*inch, PAGE_HEIGHT - 40, "Laboratorio de Diagnóstico")
		canvas.setFont('Existence-Light', 16)
		canvas.drawString(0.75*inch, PAGE_HEIGHT - 60, "Dr.Raul Chifflet")
		contacto_parts = ["El Esquilador 138 - Casilla de Correo 155", "(9420) Río Grande, Tierra del Fuego", "TEL: (02964) 441429 / 441024", "E-mail: laboratorio@asociacionruraltdf.org"]
		canvas.setFont("Ubuntu-M", 9)
		y=PAGE_HEIGHT-35
		for part in contacto_parts:
			canvas.drawRightString (PAGE_WIDTH - 0.75*inch, y, part)
			y=y-10
		canvas.setLineWidth(1.0) 
		canvas.line (0.70*inch, PAGE_HEIGHT-75 , PAGE_WIDTH-50, PAGE_HEIGHT-75) #horizontal
		canvas.restoreState()

	def solicitud(canvas):
		canvas.saveState()
		canvas.setFont('Helvetica-Bold', 15)
		canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-100, "Hoja de Trabajo")

		establ= instance.solicitud.establecimiento
		prop=instance.solicitud.establecimiento.propietario
		renspa= instance.solicitud.establecimiento.RENSPA
		vet= instance.solicitud.veterinario
		solicitud_parts  = ["Establecimiento: %s" %(establ), "Propietario: %s" %(prop), "R.E.N.S.P.A.: %s" %(renspa), "Veterinario: %s" %(vet)]
		canvas.setFont("Helvetica", 9)
		y=PAGE_HEIGHT-120
		for part in solicitud_parts:
			canvas.drawString (0.75*inch, y, part)
			y=y-10

		fecha="22/10/2010"
		motivo= instance.solicitud.motivo
		protocolo=instance.protocolo
		solicitud_parts  = ["Fecha Recepción: %s" %(fecha), "Motivo: %s" %(motivo), "N° de Protocolo: %s" %(protocolo)]
		canvas.setFont("Helvetica", 9)
		y=PAGE_HEIGHT-120
		for part in solicitud_parts:
			canvas.drawString (PAGE_WIDTH/2.0, y, part)
			y=y-10

		canvas.restoreState()

	#Definimos las caracteristicas fijas de la primera página
	def myFirstPage(canvas, doc):
		encabezado(canvas)
		solicitud(canvas)
		canvas.saveState()
		# pie de pagina:
		canvas.setFont('Times-Roman', 9)
		canvas.drawString(inch, 0.75 * inch, "Primera pagina / Laboratorio de Diagnóstico Dr. Raul Chifflet")
		canvas.restoreState()

	#Definimos disposiciones alternas para las caracteristicas de las otras páginas
	def myLaterPages(canvas, doc):
		canvas.saveState()
		encabezado(canvas)
		# pie de pagina
		canvas.setFont('Times-Roman', 9)
		canvas.drawString(inch, 0.75 * inch, "Página %d / Laboratorio de Diagnóstico Dr. Raul Chifflet" %(doc.page))
		canvas.restoreState()

	def cuerpo(canvas):
		#Iniciamos el story para los registros
		Story = [Spacer(1, 80)]
		title = instance.diagnostico.descripcion
		
		p = Paragraph(title, tit2)
		Story.append(p)
		Story.append(Spacer(1, 12))
		
		#Definimos un estilo
		style = styles["Normal"]
		Story.append(Spacer(1, 12))

		for key, value in grupos.items():
			for v in value:
				header = Paragraph(key, tit2)
				Story.append(header)
				Story.append(Spacer(1, 12))
				headings = ["#Id", ]
				for p in v:
					headings.append(p.descripcion)
					headings.append("u.")
				allregistros = []
				for i in all_indiv_de_solic:
					registros=[]
					registros.append(i.individuoPadre.identificacion)
					for p in v:
						registros.append("")
						registros.append(p.unidadmedida)
					allregistros.append(registros)
					#print(allregistros)
				t = Table([headings] + allregistros)
				t.setStyle(TableStyle(
					[
						('GRID', (0,0), (10, -1), 1, colors.dodgerblue),
						('LINEBELOW', (0,0), (-1, 0), 2, colors.darkblue),
						('BACKGROUND', (0,0), (-1, 0), colors.dodgerblue)
					]
				))
				Story.append(t)
				Story.append(Spacer(1, 12))
		
		for g in grupo_list_i:
			header=Paragraph(g.grupo, tit2)
			Story.append(header)
			Story.append(Spacer(1, 12))

			for p in all_param_del_diag:
				if g.grupo == p.grupo:
					item_p = Paragraph(p.descripcion+": ____________________", style) 
					Story.append(item_p)


		Story.append(Spacer(1, 12))
		return Story

	Story = cuerpo(canvas)
	#Creamos un documento basándonos en una plantilla
	doc = SimpleDocTemplate(buff, pagesizes=A4, rightMargin=72, 
							leftMargin=72, topMargin=72, bottomMargin=75)
	#Construimos el documento a partir de los argumentos definidos
	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
	#doc.build(Story)
	response.write(buff.getvalue())
	buff.close()
	return response

def tercerizar(request, id=None):
	instance_dap = get_object_or_404(DetalleAnalisisPadre, id=id)
	ter = Tercerizacion.objects.all().filter(detalleanalisispadre=instance_dap)
	# Aca comienza la configuracion del PDF
	response = HttpResponse(content_type='application/pdf')
	pdf_name = "tercerizacion_%s.pdf" %instance_dap.protocolo
	response['Content-Disposition'] = 'filename=%s; pagesize=A4' %pdf_name

	buff = BytesIO()
	
	def encabezado(canvas):
		canvas.saveState()
		canvas.setFont('Existence-Light', 22)
		canvas.drawString(0.75*inch, PAGE_HEIGHT - 40, "Laboratorio de Diagnóstico")
		canvas.setFont('Existence-Light', 16)
		canvas.drawString(0.75*inch, PAGE_HEIGHT - 60, "Dr.Raul Chifflet")
		contacto_parts = ["El Esquilador 138 - Casilla de Correo 155", "(9420) Río Grande, Tierra del Fuego", "TEL: (02964) 441429 / 441024", "E-mail: laboratorio@asociacionruraltdf.org"]
		canvas.setFont("Ubuntu-M", 9)
		y=PAGE_HEIGHT-35
		for part in contacto_parts:
			canvas.drawRightString (PAGE_WIDTH - 0.75*inch, y, part)
			y=y-10
		canvas.setLineWidth(1.0) 
		canvas.line (0.70*inch, PAGE_HEIGHT-75 , PAGE_WIDTH-50, PAGE_HEIGHT-75) #horizontal
		canvas.restoreState()

	def solicitud(canvas):
		canvas.saveState()
		canvas.setFont('Ubuntu-B', 15)
		title = "Tercerizacion de Protocolo N°%d" %instance_dap.protocolo.numero
		canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-100, title)

		establ= instance_dap.solicitud.establecimiento
		prop=instance_dap.solicitud.establecimiento.propietario
		renspa= instance_dap.solicitud.establecimiento.RENSPA
		vet= instance_dap.solicitud.veterinario
		solicitud_parts  = ["Establecimiento: %s" %(establ), "Propietario: %s" %(prop), "R.E.N.S.P.A.: %s" %(renspa), "Veterinario: %s" %(vet)]
		canvas.setFont("Helvetica", 9)
		y=PAGE_HEIGHT-130
		for part in solicitud_parts:
			canvas.drawString (0.75*inch, y, part)
			y=y-10

		fecha="22/10/2010"
		motivo= instance_dap.solicitud.motivo
		protocolo=instance_dap.protocolo
		solicitud_parts  = ["Fecha Recepción: %s" %(fecha), "Motivo: %s" %(motivo), "N° de Protocolo: %s" %(protocolo)]
		canvas.setFont("Helvetica", 9)
		y=PAGE_HEIGHT-130
		for part in solicitud_parts:
			canvas.drawString (PAGE_WIDTH/2.0, y, part)
			y=y-10

		canvas.restoreState()


	#Definimos las caracteristicas fijas de la primera página
	def myFirstPage(canvas, doc):
		encabezado(canvas)
		solicitud(canvas)
		canvas.saveState()
		# pie de pagina:
		canvas.setFont('Times-Roman', 9)
		canvas.drawString(inch, 0.75 * inch, "Primera pagina / Laboratorio de Diagnóstico Dr. Raul Chifflet")
		canvas.restoreState()

	#Definimos disposiciones alternas para las caracteristicas de las otras páginas
	def myLaterPages(canvas, doc):
		canvas.saveState()
		encabezado(canvas)
		# pie de pagina
		canvas.setFont('Times-Roman', 9)
		canvas.drawString(inch, 0.75 * inch, "Página %d / Laboratorio de Diagnóstico Dr. Raul Chifflet" %(doc.page))
		canvas.restoreState()

	def cuerpo(canvas):
		Story = [Spacer(1, 150)]
		style = styles["Normal"]
		print(ter)
		for t in ter:
			f_e=str(t.fecha_envio)
			print(f_e)
			print(type(f_e))
			fecha_envio = Paragraph("Fecha de Envío: "+f_e, style) 
			Story.append(fecha_envio)
			Story.append(Spacer(1, 12))
			f_d=str(t.fecha_devolucion)
			fecha_devolucion = Paragraph("Fecha de Devolución: "+f_d, style)
			Story.append(fecha_devolucion)
			Story.append(Spacer(1, 12))
			institucion = Paragraph("Institución a la que se envia: "+t.institucion, style) 
			Story.append(institucion)
			Story.append(Spacer(1, 12))

		return Story

	Story = cuerpo(canvas)
	#Creamos un documento basándonos en una plantilla
	doc = SimpleDocTemplate(buff, pagesizes=A4, rightMargin=72, 
							leftMargin=72, topMargin=72, bottomMargin=75)
	#Construimos el documento a partir de los argumentos definidos
	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
	

	#doc.build(Story)
	response.write(buff.getvalue())
	buff.close()
	return response

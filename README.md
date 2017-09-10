# blacksheep
27-08-2017

https://stackoverflow.com/questions/1377446/render-html-to-pdf-in-django-site
http://pythonpiura.org/posts/2016/05/13/reporte-pdf-en-django-con-reportlab/

OBJETIVOS:
- delete setedar desde el views que cambie estado de activo a false
- HTML: Hoja_de_Trabajo, EliminarProtocolo & Tercerizacion: falta guardar y generar informes/Hoja en PDF

##- Trasladar datos de SolAn.html a Protocolo, y a  Individuo Padre (por views)
- Hacer en HTML: 
## + Cargar_Resulatados (desde ahi generar los PDF para imprimir HDT): ver que corte el grupo de parametros cada "x" parametros
- en /DetalleAnalisisPadre/(id)/:
##- en AltaIndividuoPadre.html: lista número de órden que sea autoincremental (JS)

- en alta de protocolo, los diagnosticos que propone deberian ser segun la muestra
- Alta Diagnostico: 
 	+ vista previa: Boton junto a "guardar" & modal(html)
- en ver_detAn.html: columna "Estado"
- PDF a generar: (o exel)
	+ HDT Vacía
	+ INFORMES
	+ TERCERIZACION
	+ ELIMINACION DE PROTOCOLO
- User --> login --> Menu
- Actualizar modificaciones en la carpeta de proyecto

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
hecho:
-- en detalle de diagnostico, que muestre:
		GRUPO DE PARAMETRO 1
			* PARAMETRO 1
			* PARAMETRO 2
		GRUPO DE PARAMETRO 2
			* PARAMETRO 3
			* PARAMETRO 4
+ Boton "Eliminar Protocolo" (tiene que trasladar la info del protocolo)

#############################################
#											#
# para la creacion de PDF instalar libreria	#
# pip3 install reportlab					#
# 											#
#############################################

* para incluir imagenes en PDF, revisar libreria Pillow  (pip3 install Pillow)








Se arreglan con jquery {

	HECHO -- Valores de referencia popup de diagnostico, para unificar parametros, diagnostico y especie y que los datos queden guardados al cerrar el popup
	
	-- especie en valores por referencia pueda ser 0 por defecto

	** tabla parametros si se selecciona boolean se desactiva valores de referencia: REVISAR PORQUE FUNCIONA SOLO EN LA 1° LINEA, PERO EN LOS QUE SE AGREGAN YA NO FUNCIONA

}

HECHO -- en la carga de "chiquiteses", verificar que cada cosa se cargue una sola vez. Por ejemplo, en Muestra no puedo cargar "Sangre" dos veces. Setear el model para que sea "unique".

HECHO -- agregar en models campo "activo" de tipo Boolean para intercambiar el valor de activo a inactivo al eliminar --> agregado a todos los models del BSAdmin

--> hacer tabla de registro de actividades que guarde: las acciones de los usuarios y admin. quien? que? cuando?

--> controlar los delete si esta siendo utilizado o en que estado se encuentra(true-false)

AGREGAR EN CARPETA:
- cambios en models de "nombre" a "descripcion" (raza y categoriaE)
- CAMBIOS EN MODELS DE VALORES UNIQUE
- agregar en models campo "activo" de tipo Boolean para intercambiar el valor de activo a inactivo al eliminar
- agregar el campo grupos en models parametros y en las tablas de BDD
- Valores de referencia esta planteado en la carpeta como una pagina mas, pero nosotros lo estamos haciendo como pop-up(modal)

 Necesitamos un jqueru para preguntar si esta seguro de la accion que va a realizar (principalmente para los eliminar grandes)
//window.confirm(); 
 Vistaprevia de diagnostico finalizado
// this es la posicion donde fue clickeado el boton, sin importar las veces que se repita
	
nueva palabra: OPTIMIZACION, codigo limpio
PoC : Pruebas de Concepto (Proof of Concept)

youtube: django 1.9 tutorial how to turn data to json ot xml






-- views y urls de bsuser
-- en diagnostico "VISTA PREVIA" en un modal que arregle los datos cargados para previsualizar Hoja de Trabajo


a futuro:
HECHO-- tipo de datos: arreglar visualmente
# blacksheep

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

29-10-17 - Tareas Pendientes:

faltan valores de referencia en los infromes en la parte de las tablas. donde lo pongo?? con titulo de Valores de Referencia y despues items con cada parametro.

EN VALIDACIONES & MODELS :

en DAP.valor = textinput max_length=10 caracteres


- En "Registrar Protocolos":
	X* Falta que no repita las muestras ni los diagnosticos
	X* los diagnosticos que propone deberian ser segun la muestra

- En CARPETA:
	* ver asociaciones de extension e inclusion de CDU
	* hay que hacer CDU de los listados???

- Hoja de Trabajo (PDF): agregar las observaciones que se cargaron en Solicitud de Analisis
-DetalleAnalisis :  el boton "tercerizar" tiene que estar activo solo cuando el estado del diagnostico sea "Completo"

- Tercerizar : 
	* en modificar: Validar fechas (que fecha de devolucion sea posterior a de envio)
	* En alta, sacar fecha de devolucion, que solo este cuando se desee modificar.

- Eliminar Protocolo:
	* no tiene que mostrar el imput con el n° de protocolo (debe mandarse en el formulario como hidden)

- guardar datos Trasladados de SolAn.html a Protocolo, y a  Individuo Padre (por views)

- en los detalles ver que no diga el Estado "Activo"

- en vez del Http404 crear una pag que diga que para entrar se necesita loguear con otro usuario lab/admin. poner dos botones: 
	* desloguearse y loguearse comonotro usuario
	* volver


&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
- User --> Menu: menu correspondiente, botod de logout, nombre del ususario logueado
- BDD :  que los registros no se guarden en mayusculas: ver en models self description upper
- En "Cargar Individuos":
	* la Raza tiene que filtrarse por la Especie seleccionada en Solicitud de Analisis
en Diagnostico.piepagina = textinput max_length=100 caracteres
en SolicitudAnalisis.obs = textinput max_length=85 caracteres
en Parametros.descripcion = textinput max_length=15 caracteres
en Parametros.unidad de medida = textinput max_length=5 caracteres
en valores de referencia = textinput max_length=15 caracteres
	ok* En verificacion tiene que avisazr que si el numero de protocolo ya fue usado previamente (si ya hay uno guardado en BDD)
	ok* Cuando no hay protocolos que emita mensaje de error y no permita irse de la pagina.
	OK* Verificar que no se repitan las identificaciones de los individuos en la misma carga (no importa si ya esta en BDD)
	OK* Actualizar numeracion de los individuos automaticamente
OK- Alta Establecimiento: que no se cargue CUIT y RENSPA si ya fue cargado (si esta en BDD)

27-08-2017

https://stackoverflow.com/questions/1377446/render-html-to-pdf-in-django-site
http://pythonpiura.org/posts/2016/05/13/reporte-pdf-en-django-con-reportlab/

OBJETIVOS:

##- HTML: Hoja_de_Trabajo, EliminarProtocolo & Tercerizacion: falta guardar y generar informes/Hoja en PDF

- Hacer en HTML: 
## + Cargar_Resulatados (desde ahi generar los PDF para imprimir HDT): 
- en /DetalleAnalisisPadre/(id)/:
##- en AltaIndividuoPadre.html: lista número de órden que sea autoincremental (JS)

- Alta Diagnostico: 
 	+ vista previa: Boton junto a "guardar" & modal(html)
- en ver_detAn.html: columna "Estado"
- PDF a generar: (o exel)
	+ INFORMES
- Actualizar modificaciones en la carpeta de proyecto

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
hecho:
	+ HDT Vacía
	+ TERCERIZACION
	+ ELIMINACION DE PROTOCOLO
- ver que corte el grupo de parametros cada "x" parametros
- delete setedar desde el views que cambie estado de activo a false
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
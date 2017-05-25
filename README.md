# blacksheep

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

youtube: django 1.9 tutorial how to turn data to json ot xml






-- views y urls de bsuser
-- en diagnostico "VISTA PREVIA" en un modal que arregle los datos cargados para previsualizar Hoja de Trabajo


a futuro:
-- en detalle de diagnostico, que muestre:
		GRUPO DE PARAMETRO 1
			* PARAMETRO 1
			* PARAMETRO 2
		GRUPO DE PARAMETRO 2
			* PARAMETRO 3
			* PARAMETRO 4
-- tipo de datos: arreglar visualmente
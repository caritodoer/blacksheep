# blacksheep
RESUELTOS:
12-3-17 : 
los modificar no muestran los datos. Trae la info y la vuelve a guardar, pero no se ven los datos a modificar.--> en bootstrap
Activo de veterinario OK, y disabled  // arreglado checked disabled en el input


Se arreglan con jquery {


	ADRIAN Select
	--> Otros datos(veterinario)
	LEO indicar erorres del Form en html 
	LEO & ADRIAN indicar que tiene que tener un checkbox marcado (veterinario, establecimiento)
	--> Ver como generar los "botones de agregar" en diagnostico
	ADRIAN Checkbox de veterinario Hacer // como se hace
	indicar que tiene que tener un checkbox marcado (veterinario, establecimiento)

	Ver como generar los "botones de agregar"
	**revisar diagnostico > select de tipo de dato (parametros)


	Valores de referencia popup de diagnostico, para unificar parametros, diagnostico y especie
	y que los datos queden guardados al cerrar el popup
	especie en valores por referencia pueda ser 0 por defecto

	** tabla parametros si se selecciona boolean se desactiva valores de referencia


	pasar valores de django a jquery para agregar el selected o checked

-- en la carga de "chiquiteses", verificar que cada cosa se cargue una sola vez. Por ejemplo, en Muestra no puedo cargar "Sangre" dos veces. Setear el model para que sea "unique".
}

{{ form }}


++ Si los json no vienen ordenados agregar .order_by('id') ++

como traer datos con json + ajax

como guardar dos form juntos y anidados 

nueva palabra: OPTIMIZACION, codigo limpio
youtube: django 1.9 tutorial how to turn data to json ot xml
taller jquery por alex arriaga

** cuando usamos la lista, evitar cualquier "espaciado" innecesario
AGREGAR EN CARPETA:
- cambios en models de "nombre" a "descripcion" (raza y categoriaE)
- agregar el campo grupos en models parametros y en las tablas de BDD
- Valores de referencia esta planteado en la carpeta como una pagina mas, pero nosotros lo estamos haciendo como pop-up(modal)


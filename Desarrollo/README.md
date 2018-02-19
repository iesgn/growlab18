# Equipo de Desarrollo.

Esta es la carpteda del repositorio donde vamos a plantear y programar el algoritmo de la **agenda inteligente**

1. Por el momento hemos definido algunas **funciones** basicas para tratar la informacion:
* **Ingresar Eventos**: Funcion que recorre un fichero de texto (donde definimos diferentes eventos) para ahorrarnos introducir uno a uno los eventos en las pruebas.
* **Generar Tabla Dia**: Genera una lista vacia con el numero de huecos en un dia. Determinado y calculado con la constante *SEG_TEMP*.
* **Imprimir Dia**: Muestra de forma clara por pantalla la organizacion de un dia.
* **Calcular Candidatos**: En funcion de la constante de tiempo genera un entero con el numero de todos los candidatos posibles.
* **Generar Candidatos**: Genera una lista ordenada cronologicamente de todos los candidatos de un evento.
* **Tabla TemPri**: Genera una lista de listas de diccionario ordenadas por prioridad. habria que ordenar tambien por horas?

	* **Notas:** He ampliado el uso de datatime en la mayoria de funciones, y progresado en las funciones *Generar Candidatos* y *Tabla Tempri*. 
		*Generar Candidatos* aun no funciona como se espera, problemas al sumar el segmento de tiempo, en la linea `dic["hora_inicio"]+=timedelta(minutes=(SEG_TEMP*x))`.
		*Tabla Tempri* aun no ha sido probada debido al fallo de *Generar Candidatos*
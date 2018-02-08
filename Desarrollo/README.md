# Equipo de Desarrollo.

Esta es la carpteda del repositorio donde vamos a plantear y programar el algoritmo de la **agenda inteligente**

Por el momento hemos definido algunas **funciones** basicas para tratar la informacion:
* **Ingresar Eventos**: Funcion que recorre un fichero de texto (donde definimos diferentes eventos) para ahorrarnos introducir uno a uno los eventos en las pruebas.
* **Generar Tabla Dia**: Genera una lista vacia con el numero de huecos en un dia. Determinado y calculado con la constante *SEG_TEMP*.
* **Imprimir Dia**: Muestra de forma clara por pantalla la organizacion de un dia.
* **Calcular Candidatos**: En funcion de la constante de tiempo genera un entero con el numero de todos los candidatos posibles.
* **Generar Candidatos**: Genera una lista ordenada cronologicamente de todos los candidatos de un evento.
* **Tabla TemPri**: Genera una lista de listas de diccionario ordenadas por prioridad. habria que ordenar tambien por fecha?
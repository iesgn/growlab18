# Equipo de Desarrollo.

Esta es la carpteda del repositorio donde vamos a plantear y programar el algoritmo de la **agenda inteligente**

Por el momento hemos definido algunas **funciones** basicas para tratar la informacion:

#### **Ingresar Eventos**: 
Funcion que recorre un fichero de texto (donde definimos diferentes eventos) para ahorrarnos introducir uno a uno los eventos en las pruebas. Los eventos se guardan en una **Lista** de **Diccionarios** formados por los siguientes campos:
* nombre
* periodo
* prioridad
* duracion
* fecha de inicio
* fecha final
* hora de inicio
* hora de fin

#### **Generar Tabla Dia**: 
Genera una **Lista** de **Listas** donde el tamano de la **lista** esta determinado y calculado con la constante *SEG_TEMP*. Y las **listas** dentro de la lista estan compuestas por dos campos. **Fecha** y **Hueco para Candidato**
	
`dia=[[fecha1,None],[fecha2,None],...]` 

#### **Imprimir Dia**: 
Muestra de forma clara por pantalla la organizacion de un dia.

#### **Calcular Candidatos**: 
En funcion de la constante de tiempo, retorna un **entero** con el numero de todos los candidatos posibles.

#### **Generar Candidatos**: 
Genera una **lista** ordenada cronologicamente de todos los candidatos de un evento.

#### **Tabla TemPri**: 
Genera una **lista** de **listas** de **diccionario** ordenadas por prioridad y tiempo. Estructura:
	
`[[candidato1,candidato2,...],[...],[...]]`

Dentro de la **Lista Principal** encontramos **tres** listas (correspondientes a cada nivel de **prioridad**). Dentro de esas tres **listas** encontramos cada uno de los **candidatos** ordenados cronologicamente.

#### **Busqueda Profunda**
Rellena la tabla del dia. Rellena con el **candidato correcto** todos los segmentos que corresponda en funcion de su duracion. Devuelve la **tabla dia** (**lista de listas**) con el siguiente formato:
	
`dia=[[fecha1,None],[fecha2,Candidato],...]` 
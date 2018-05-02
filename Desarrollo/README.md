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

## Documentación para la memoria

### /login
En la ruta "login" tenemos la función que permite que los usuarios inicien sesión en el servicio.
Aquí, lo que hacemos será una consulta a la base de datos. Si los datos introducidos son correctos, se iniciará sesión y se redirigirá al usuario a la página principal. Si no, saldrá un mensaje de error comunicándonos que los datos introducidos son incorrectos.

### /registro
Esta es la función que permite el registro de nuevos usuarios en el servicio.
Se pedirá al usuario que introduzca un nombre de usuario, un email y una contraseña, la cual tendrá que repetir para asegurarse de que la ha introducido correctamente. Los datos enumerados anteriormente serán obligatorios; si el usuario no los introduce, no nos dejará avanzar.
Si el usuario se crea correctamente, se redirigirá al usuario a la pantalla de **login** para que pueda iniciar sesión junto con un mensaje que le dice que el usuario ha sido creado correctamente. Si el usuario por el contrario no se ha podido crear, volverá a mostrar la página de registro con un mensaje de error.

### /logout
Esta función termina la sesión del usuario que está conectado en ese momento al servicio y redirige a la página principal.

### /eventos
Esta función muestra todos los eventos del usuario registrado en forma de "tarjetas".

### /eventos/add
A través de un formulario, esta función introduce un evento en la base de datos.
Una vez introducido correctamente el evento, nos redirigirá a la página **eventos**, donde podremos visualizarlo junto con los demás eventos del usuario actual, si es que tuviera.

### /eventos/del
Borra un evento determinado.

### /eventos/edit
Esta función nos permitirá editar un evento concreto.

### /calendar
Nos muestra el calendario con los distintos eventos que hemos introducido anteriormente.

Las páginas /eventos, /eventos/add, /eventos/del, /eventos/edit y /calendar sólo se podrán acceder en el caso de que haya un usuario conectado al servicio en ese momento. De lo contrario, nos redirigiría a la pantalla de **login**

# grow-lab - ec2ce - Protato

## app.py

Es el programa principal de nuestra aplicación web escrita en Flask. En
este fichero declaramos la lógica (controlador) de nuestra aplicación, indicando
las diferentes rutas de la aplicación y las funciones que se ejecutan cada vez
que accedemos a una de ellas.

## agenda.py

Librería de funciones python que realizan la seleccion y el reparto de eventos
candidatos a partir de la programación de eventos.

## fullcalendar.py

Librería python que contiene la función que obtiene la información necesaria para que el script fullcalendar sea capaz de visualizar los eventos. Recibe la fecha inicial y final de los días en las que tiene que generar los eventos y utiliza las funciones de la librería `agenda.py` para seleccionar los eventos diarios que debe mostrar.

## basedatos.py

Librería python que tiene la función que nos permite realizar las
consultas a la bse de datos MySQL.

## templates

En este directorio se encuentran las distintas plantillas *html jinja2* para generar las páginas webs dinámicas que necesita nuestra aplicación.

* **base.html:** Plantilla base de la aplicación, todas las demás plantillas van a ser
una herencia de esta. Posee la parte común de todas las páginas, como la sección `head` del documento HTML y el píe de página.
* **menu.html:** La sección de navegación de nuestra página se encuentra en esta plantilla que se incluye en la anterior.
* **index.html:** Página principal de la aplicación, se extiende a partir de base.html y muestra información de la aplicación, con las distintas opciones que tenemos a nuestra disposición.
* **login.html:** Página web que muestre el formulario para que un usuario pueda autentificarse.
* **registro.html:** Página web que muestre el formulario para que un usuario pueda registrarse en la aplicación.
* **eventos.html:** Página web que visualiza los eventos programados para un determinado usuario.
* **addeventos.html:** Página web que visualizar el formulario para dar de alta o modificar une evento en la programación de un usuario.

## static

Aqui encontramos el contenido estático de nuestra aplicación. Como las hojas de estilo ***css***, todos los scipts de ***fullcalendar.io*** para la visualización de la agenda y la carpeta con todas las imagenes ***img***.

## requirements.txt

Librerias python necesarias para que la aplicación funcione. En un formato compatible para que se puedan generar automáticamente un entorno virtual.
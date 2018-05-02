from flask import Flask
from flask import render_template,request,redirect,session
import json
import datetime
import fullcalendar
app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def inicio():
    return render_template("index.html")

##Usuarios

@app.route('/login')
def login():
    if request.method=="GET":
          return render_template("login.html")
    else:
        #Busco en la base de datos y si existe usuario y contraseña, inicio la sesión
        pass
 
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method=="GET":
        return render_template("registro.html")
    else:
        #Compruebo que el usuario no exista.
        #Si no existe lo añado a la BD
        pass

@app.route('/logout')
def logout():
    session.pop("usuario",None)
    return redirect("/")

#Programación de eventos

@app.route('/eventos')
def eventos():
    # Visualiza una plantilla donde enviamos todos los eventos del usuario registrado
    return render_template("eventos.html")


@app.route('/eventos/add')
def addeventos():
    # Visualiza una plantilla donde leemos los datos del evento
    if request.method=="GET":
        return render_template("addeventos.html")
    else:
        #Añado el evento a la BD
        pass

@app.route('/eventos/del/<cod>')
def deleventos(cod):
    # Borra el evento de la base de datos
    pass



#Calendario

@app.route('/calendar')
def calendar():
    return render_template("agenda.html")

@app.route('/data')
def return_data():
    finicio = request.args.get('start', '')
    ffinal = request.args.get('end', '')
    events=fullcalendar.geteventos(finicio,ffinal)  
    return json.dumps(events)


if __name__ == '__main__':
    app.debug = True
    app.run()

from flask import Flask
from flask import render_template,request,redirect,session
from basedatos import run_query
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
          return render_template("login.html", exito=None)
    else:
          email = request.form['email']
          pass1 = request.form['pass1'] 
          con_login=run_query('select usuario from usuarios where e_mail="{}" and contraseña="{}"'.format(email,pass1))
        #Busco en la base de datos y si existe usuario y contraseña, inicio la sesión
        pass
 
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method=="GET":
        return render_template("registro.html",datos=None,error=None)
    else:
        usuario = request.form['usuario']
        email = request.form['email']
        pass1 = request.form['pass1'] 
        pass2 = request.form['pass2']
        con_user=run_query('select count(*) from usuarios where usuario="{}"'.format(usuario))
        con_email=run_query('select count(*) from usuarios where e_mail="{}"'.format(email))
        print(con_user[0][0])
        print(con_email[0][0])
        if pass1!=pass2:
            error="Las contraseñas no coinciden."
            return render_template("registro.html",datos=request.form,error=error)
        elif con_user[0][0]!=0:
            error="El usuario ya existe en la base de datos."
            return render_template("registro.html",datos=request.form,error=error)
        elif con_email[0][0] != 0:
            error="El email ya existe en la base de datos."
            return render_template("registro.html",datos=request.form,error=error)
        else:
            run_query('insert into usuarios values("{}", "{}", "{}")'.format(email, usuario, pass1))
            exito="Se ha creado el usuario correctamente. Inicia sesión para poder empezar a usar la mejor agenda del mundo :)"
            return render_template("login.html", exito=exito)
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
    events,errores  =fullcalendar.geteventos(finicio,ffinal)  
    return json.dumps(events)


if __name__ == '__main__':
    app.debug = True
    app.run()

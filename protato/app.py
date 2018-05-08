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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="GET":
          return render_template("login.html", exito=None,error=None)
    else:
        email = request.form['email']
        pass1 = request.form['pass1'] 
        con_login=run_query('select usuario,e_mail from usuarios where e_mail="{}" and contraseña="{}"'.format(email,pass1))
        #Busco en la base de datos y si existe usuario y contraseña, inicio la sesión
        
        if con_login!=():
            session["usuario"]=con_login[0][0]
            session["email"]=con_login[0][1]
            return redirect("/")
        else:
            error="Datos incorrectos."
            return render_template("login.html", exito=None,error=error)

 
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
    session.pop("email",None)
    return redirect("/")

#Programación de eventos

@app.route('/eventos')
def eventos():
    #No autorizo si no hay un usuario logueado
    if not "usuario" in session:
        return redirect('/login')
    else:
        # Visualiza una plantilla donde enviamos todos los eventos del usuario registrado
        datos = run_query('select * from eventos where e_mail="{}"'.format(session['email']))
        return render_template("eventos.html", datos = datos)



@app.route('/eventos/add', methods=['GET', 'POST'])
def addeventos():
    #No autorizo si no hay un usuario logueado
    if not "usuario" in session:
        return redirect('/login')
    else:
        # Visualiza una plantilla donde leemos los datos del evento
        if request.method=="GET":
            return render_template("addeventos.html",datos=None,error=None,boton="Crear Evento",url="/eventos/add")
        else:
            #Añado el evento a la BD
           
            titulo = request.form['titulo']
            desc = request.form['descripcion']
            periodo = request.form['periodo']
            duracion = request.form['duracion']
            prioridad = request.form['prioridad']
            mastarde = request.form['mastarde']
            fechaini = request.form['fechaini']
            fechafin = request.form['fechafin']
            horaini = request.form['horaini']
            horafin = request.form['horafin']
            fi=datetime.datetime.strptime(fechaini, "%Y-%m-%d")
            ff=datetime.datetime.strptime(fechafin, "%Y-%m-%d")
            hi=datetime.datetime.strptime(horaini, "%H:%M")
            hf=datetime.datetime.strptime(horafin, "%H:%M")
            if ff<fi:
                error="La fecha final debe ser mayor que la inicial."
                return render_template("addeventos.html",datos=request.form,error=error,boton="Crear Evento",url="/eventos/add")
            if hf<hi:
                error="La hora final debe ser mayor que la inicial."
                return render_template("addeventos.html",datos=request.form,error=error,boton="Crear Evento",url="/eventos/add")
            if hi.minute%5!=0 or hf.minute%5!=0:
                error="Las horas deben ser múltiplos de 5 minútos."
                return render_template("addeventos.html",datos=request.form,error=error,boton="Crear Evento",url="/eventos/add")
            
            sql='insert into eventos (E_MAIL,TITULO,DURACION,DESCRIPCION,FECHAINI,FECHAFIN,HORAINI,HORAFIN,PERIODO,PRIORIDAD,MASTARDE) values("{}", "{}", {}, "{}", "{}", "{}", "{}", "{}", "{}", {}, "{}")'.format(session["email"],titulo,duracion,desc,fechaini,fechafin,horaini,horafin,periodo,prioridad,mastarde)
            
            run_query(sql)
            
            return redirect("/eventos")
            

@app.route('/eventos/del/<cod>')
def deleventos(cod):
    #No autorizo si no hay un usuario logueado
    if not "usuario" in session:
        return redirect('/login')
    else:
        # Borra el evento de la base de datos
        sql='delete from eventos where codigo={}'.format(cod)
        run_query(sql)
        return redirect("/eventos")

@app.route('/eventos/edit/<cod>', methods=['GET', 'POST'])
def editeventos(cod):
    #No autorizo si no hay un usuario logueado
    if not "usuario" in session:
        return redirect('/login')
    else:
        if request.method=="GET":
            # Borra el evento de la base de datos
            sql='select * from eventos where codigo={}'.format(cod)
            res=run_query(sql)
            res=res[0]
            datos={}
            datos["titulo"] = res[2]
            datos["desc"] = res[4]
            datos["periodo"] = res[9]
            datos["duracion"] = res[3]
            datos["prioridad"] = res[10]
            datos["mastarde"] = res[11]
            datos["fechaini"] = res[5]
            datos["fechafin"] = res[6]
            datos["horaini"] = res[7]
            datos["horafin"] = res[8]
            
            return render_template("addeventos.html",datos=datos,error=None,boton="Modificar Evento",url="/eventos/edit/"+cod)    
        else:
            #Añado el evento a la BD
           
            titulo = request.form['titulo']
            desc = request.form['descripcion']
            periodo = request.form['periodo']
            duracion = request.form['duracion']
            prioridad = request.form['prioridad']
            mastarde = request.form['mastarde']
            fechaini = request.form['fechaini']
            fechafin = request.form['fechafin']
            horaini = request.form['horaini']
            horafin = request.form['horafin']
            fi=datetime.datetime.strptime(fechaini, "%Y-%m-%d")
            ff=datetime.datetime.strptime(fechafin, "%Y-%m-%d")
            hi=datetime.datetime.strptime(horaini, "%H:%M")
            hf=datetime.datetime.strptime(horafin, "%H:%M")
            if ff<fi:
                error="La fecha final debe ser mayor que la inicial."
                return render_template("addeventos.html",datos=request.form,error=error,boton="Modificar Evento",url="/eventos/edit/"+cod)
            if hf<hi:
                error="La hora final debe ser mayor que la inicial."
                return render_template("addeventos.html",datos=request.form,error=error,boton="Modificar Evento",url="/eventos/edit/"+cod)
            if hi.minute%5!=0 or hf.minute%5!=0:
                error="Las horas deben ser múltiplos de 5 minútos."
                return render_template("addeventos.html",datos=request.form,error=error,boton="Modificar Evento",url="/eventos/edit/"+cod)
            
            sql='update eventos set TITULO="{}",DURACION="{}",DESCRIPCION="{}",FECHAINI="{}",FECHAFIN="{}",HORAINI="{}",HORAFIN="{}",PERIODO="{}",PRIORIDAD={},MASTARDE="{}" where codigo="{}"'.format(titulo,duracion,desc,fechaini,fechafin,horaini,horafin,periodo,prioridad,mastarde,cod)
            run_query(sql)
            
            return redirect("/eventos")


#Calendario

@app.route('/calendar')
def calendar():
    #No autorizo si no hay un usuario logueado
    if not "usuario" in session:
        return redirect('/login')
    else:
        return render_template("agenda.html")

@app.route('/data')
def return_data():
    finicio = request.args.get('start', '')
    ffinal = request.args.get('end', '')
    events,errores  =fullcalendar.geteventos(finicio,ffinal,session["email"])  
    return json.dumps(events)


if __name__ == '__main__':
    app.debug = True
    app.run()

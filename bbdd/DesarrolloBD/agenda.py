import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'debian'
DB_PASS = 'debian'
DB_NAME = 'agenda'

def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*datos) # Conectar a la base de datos
    cursor = conn.cursor()         # Crear un cursor
    cursor.execute(query)          # Ejecutar una consulta

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()   # Traer los resultados de un select
    else:
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None

    cursor.close()                 # Cerrar el cursor
    conn.close()                   # Cerrar la conexión

    return data


query="select USUARIO from usuarios;"
datos=run_query(query)

for usu in datos:
	print(usu[0])

criterio=input("Dime el nombre del usuario para ver los eventos: ")

query="select TITULO, NOMBRE, COD_PRIORIDAD, DURACION, date_format(FECHAINI, '%d/%m/%Y'), date_format(FECHAFIN, '%d/%m/%Y'), date_format(FECHAINI, '%H:%i'), date_format(FECHAFIN, '%H:%i') from eventos e, periodos p where COD_PERIODO=p.CODIGO and E_MAIL = (select E_MAIL from usuarios where usuario='{}');".format(criterio)
datos=run_query(query)

eventos=[]
for evento in datos:
	dic={}
	dic["nombre"]=evento[0]
	dic["periodo"]=evento[1]
	dic["prioridad"]=evento[2]
	dic["duracion"]=evento[3]
	dic["fecha_inicio"]=evento[4]
	dic["fecha_fin"]=evento[5]
	dic["hora_inicio"]=evento[6]
	dic["hora_fin"]=evento[7]
	eventos.append(dic)
print(eventos)

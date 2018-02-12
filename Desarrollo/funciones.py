from datetime import datetime, timedelta

SEG_TEMP=5 				# constante de tiempo (EN MINUTOS) para "segmentar" el dia
FORMATO = "%H:%M"		# Formato para la funcion datetime

# Voy a hacer un fichero de texto con varios eventos para ahorrarme el escribirlo por pantalla
# estructura del archivo: nombre, periodo, prioridad, duracion, fecha_inicio, fecha_fin, hora_inicio, hora_fin
def IngresarEventos():
	eventos=[]
	with open ("eventos.txt","r") as text: 
		for evento in text:
			dic={}
			dic["nombre"]=evento.split(",")[0]
			dic["periodo"]=evento.split(",")[1]
			dic["prioridad"]=evento.split(",")[2]
			dic["duracion"]=evento.split(",")[3]
			dic["fecha_inicio"]=evento.split(",")[4]
			dic["fecha_fin"]=evento.split(",")[5]
			dic["hora_inicio"]=datetime.strptime(evento.split(",")[6], FORMATO)
			if evento.split(",")[7] != "hora_fin\n":
				dic["hora_fin"]=datetime.strptime(evento.split(",")[7].split("\n")[0], FORMATO)
			else:
				dic["hora_fin"]=datetime.strptime(evento.split(",")[6], FORMATO)	# Si no tiene hora final, le asigno la hora 
			eventos.append(dic)														# inicial para que se genere solo un candidato
	return eventos

# Genero la lista del tamano correspondiente a la constante 
def GenerarTablaDia():		
	dia=[]
	for x in range(int((60/SEG_TEMP)*24)):
		dia.append(None)
	return dia

# Funcion para imprimir la planificacion del dia	
def ImprimirDia(*args):
	for x in args:
		print("%s:%s ==> %s"%(x["hora_inicio"].hour,x["hora_inicio"].minute,x["nombre"]))

# Funcion para calcular el numero de candidatos de un evento | Retorna un entero			
def CalcularCandidatos(**kwargs):	
	candidatos = abs(((kwargs["hora_inicio"].hour*60) + kwargs["hora_inicio"].minute) - ((kwargs["hora_fin"].hour*60) + kwargs["hora_fin"].minute - int(kwargs["duracion"])))/SEG_TEMP
	return int(candidatos+1)		

# Genero una lista de diccionarios con todos los candidatos. Con la hora inicial modificada en cada candidato | Retorna una lista de diccionarios
def GenerarCandidatos(**kwargs):
	lista=[]
	for x in range (0,CalcularCandidatos(**kwargs)):
		dic=kwargs.copy()
		if x==0:
			lista.append(dic)
		else:
			dic["hora_inicio"]+=timedelta(minutes=(SEG_TEMP*x))	
			lista.append(dic)	
	return lista			

# Rellena la lista con todos los candidatos ordenados por tiempo / prioridad | Retorna una lista de listas de listas de diccionarios			
def TablaTemPri(*args):                                                                      #(No me he repetido, es asi)
	tempri=[]
	priUno=[]
	priDos=[]
	priTres=[]
	for evento in args:
		if evento["prioridad"]=="3":
			priUno.append(GenerarCandidatos(**evento))
		elif evento["prioridad"]=="2":
			priDos.append(GenerarCandidatos(**evento))	
		elif evento["prioridad"]=="1":
			priTres.append(GenerarCandidatos(**evento))	
	tempri.append(priUno)
	tempri.append(priDos)
	tempri.append(priTres)		
	return tempri

eventos=IngresarEventos()
tabla=TablaTemPri(*eventos)
# Para ver de forma clara la tabla Tempri
for x in tabla:
	for y in x:
		print(y[0]["nombre"],len(y))
	print("\n")	
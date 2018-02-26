from datetime import datetime, date, time, timedelta

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
				dic["hora_fin"]+=timedelta(minutes=(int(dic["duracion"])))			# inicial + duracion para que se genere solo un candidato
			eventos.append(dic)														
	return eventos

# Genero la lista del tamano correspondiente a la constante 
def GenerarTablaDia():		
	dia=[]
	tiempo=datetime.strptime("00:00","%H:%M")
	for x in range(int((60/SEG_TEMP)*24)):
		tiempo+=timedelta(minutes=(SEG_TEMP))
		dia.append(tiempo)
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

# Rellena la lista con todos los candidatos ordenados por tiempo / prioridad | Retorna una lista de listas de diccionarios			
def TablaTemPri(*args):                                                                     
	tempri=[]
	priUno=[]
	priDos=[]
	priTres=[]
	for evento in args:
		if evento["prioridad"]=="1":
			for candidato1 in GenerarCandidatos(**evento):
				if len(priUno)>0:
					for idx,pos1 in enumerate(priUno):
						if candidato1["hora_inicio"]<pos1["hora_inicio"]:
							priUno.insert(idx,candidato1)
							break
						elif idx==len(priUno)-1:
							priUno.append(candidato1)
							break			
				else:
					priUno.append(candidato1)		
		elif evento["prioridad"]=="2":
			for candidato2 in GenerarCandidatos(**evento):
				if len(priDos)>0:
					for idx,pos2 in enumerate(priDos):
						if candidato2["hora_inicio"]<pos2["hora_inicio"]:
							priDos.insert(idx,candidato2)
							break
						elif idx==len(priDos)-1:
							priDos.append(candidato2)
							break			
				else:
					priDos.append(candidato2)
		elif evento["prioridad"]=="3":
			for candidato3 in GenerarCandidatos(**evento):
				if len(priTres)>0:
					for idx,pos3 in enumerate(priTres):
						if candidato3["hora_inicio"]<pos3["hora_inicio"]:
							priTres.insert(idx,candidato3)
							break
						elif idx==len(priTres)-1:
							priTres.append(candidato3)
							break
				else:
					priTres.append(candidato3)
	tempri.append(priTres)	
	tempri.append(priDos)
	tempri.append(priUno)	
	return tempri
def BusquedaProfunda(*args):
	dia=GenerarTablaDia()
	#for segmento in dia:


#def SelecCandidato(*args):

eventos=IngresarEventos()
tabla=TablaTemPri(*eventos)

print(GenerarTablaDia())


# Para ver de forma clara la tabla Tempri
#for idx,x in enumerate(tabla):
	#for y in x:
	#	print(y["hora_inicio"].strftime(FORMATO),">>>>",y["nombre"])
	#print("\n")	

# FUNCION BUSQUEDA_PROFUNDA, creo que la funcion deberia recorrer 
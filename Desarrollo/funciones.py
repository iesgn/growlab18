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
		dia.append([tiempo,None])
		tiempo+=timedelta(minutes=(SEG_TEMP))
	return dia

# Funcion para imprimir la planificacion del dia	
def ImprimirDia(*args):
	for x in args:
		if x[1]==None:
			print("%s ==> vacio"%x[0].strftime(FORMATO))
		else:	
			print("%s ==> %s"%(x[0].strftime(FORMATO),x[1]["nombre"]))

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

def Rellenar(*pri,**evento):
	pri=list(pri)
	for cand in GenerarCandidatos(**evento):
		if len(pri)>0:
			for idx,pos in enumerate(pri):
				if cand["hora_inicio"]<pos["hora_inicio"]:
					pri.insert(idx,cand)
					break
				elif idx==len(pri)-1:
					pri.append(cand)
					break
		else:
			pri.append(cand)	
	return pri		

# Rellena la lista con todos los candidatos ordenados por tiempo / prioridad | Retorna una lista de listas de diccionarios			
def TablaTemPri(*args):                                                                     
	tempri=[]
	priUno=[]
	priDos=[]
	priTres=[]
	for evento in args:
		if evento["prioridad"]=="1":
			priUno=Rellenar(*priUno,**evento)
		elif evento["prioridad"]=="2":
			priDos=Rellenar(*priDos,**evento)
		elif evento["prioridad"]=="3":
			priTres=Rellenar(*priTres,**evento)

	tempri.append(priTres)	
	tempri.append(priDos)
	tempri.append(priUno)	
	return tempri
	
def BusquedaProfunda():
	dia=GenerarTablaDia()
	usado=[]
	horario=dia.copy()
	for idx,segmento in enumerate(dia):
		if segmento[1]==None:
			candidato=SelecCandidato(segmento[0],*usado)
			if candidato!=None:
				usado.append(candidato["nombre"])	
				for x in range(0,int(int(candidato["duracion"])/SEG_TEMP)+1):
					horario[idx+x].insert(1,candidato)	
	return horario
					
def SelecCandidato(hora, *usado):
	tempri=TablaTemPri(*IngresarEventos())
	for candidatos in tempri:
		for candidato in candidatos:
			if candidato["nombre"] not in usado and candidato["hora_inicio"]==hora:
				return candidato

horario=BusquedaProfunda()
ImprimirDia(*horario)

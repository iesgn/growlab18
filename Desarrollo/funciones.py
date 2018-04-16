from datetime import datetime, date, time, timedelta

SEG_TEMP=5 				# constante de tiempo (EN MINUTOS) para "segmentar" el dia
FORMATO = "%H:%M"		# Formato para la funcion datetime
LOMASTARDE=True

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
def GenerarCandidatos(*pri,**kwargs):
	lista=[]
	pri=list(pri)
	for x in range (0,CalcularCandidatos(**kwargs)):
		dic=kwargs.copy()
		if x==0:
			lista.append(dic)
		else:
			dic["hora_inicio"]+=timedelta(minutes=(SEG_TEMP*x))	
			lista.append(dic)	
	if len(pri)>0:	
		for idz,z in enumerate(pri):
			if z[0]["hora_inicio"]>lista[0]["hora_inicio"]:
				pri.insert(idz,lista)
				break
		if lista not in pri:		
			pri.append(lista)			
	else:
		pri.append(lista)			
	return pri			

# Rellena la lista con todos los candidatos ordenados por tiempo / prioridad | Retorna una lista de listas de diccionarios			
def TablaTemPri(*args):                                                                     
	tempri=[]
	priUno=[]
	priDos=[]
	priTres=[]
	for evento in args:
		if evento["prioridad"]=="1":
			priUno=GenerarCandidatos(*priUno,**evento)
		elif evento["prioridad"]=="2":
			priDos=GenerarCandidatos(*priDos,**evento)
		elif evento["prioridad"]=="3":
			priTres=GenerarCandidatos(*priTres,**evento)

	tempri.append(priTres)
	tempri.append(priDos)
	tempri.append(priUno)
	return tempri

################################################################################################

################################################################################################
	
def BusquedaProfunda(*tempri):
	tempri=list(tempri)
	error=[]
	dia=GenerarTablaDia()
	if LOMASTARDE:
		dia.reverse()
	horario=dia.copy()

	for x in range(0,3):
		while len(tempri[x])>0:
			candidato,estado=SelecCandidato(error,horario,tempri[x])
			if estado:
				seg=BuscarSeg(*horario,**candidato)
				horario=Rellenar(seg,*horario,**candidato)	
				tempri[x]=Quitar(candidato["nombre"],*tempri[x])
			else:
				error.append(candidato)
				tempri[x]=Quitar(candidato["nombre"],*tempri[x])	

	return horario, error

def SelecCandidato (error,horario, tempri):
	for bloque in tempri:
		if len(bloque)==1:
			return bloque[0], True		
	for idx,evento in enumerate(tempri):
		if LOMASTARDE:
			evento.reverse()
		for idy,candidato in enumerate(evento):
			seg=BuscarSeg(*horario,**candidato)
			if Comprobar(seg,*horario,**candidato):
				return candidato, True
		return candidato, False

def BuscarSeg(*horario,**candidato):
	for idx,x in enumerate(horario):
		if x[0]==candidato["hora_inicio"]:
			return idx

def Rellenar (seg,*horario,**candidato):
	horario=list(horario)
	for x in range(0,int(int(candidato["duracion"])/SEG_TEMP)+1):
		if LOMASTARDE:
			horario[seg-x].insert(1,candidato)	
		else:
			horario[seg+x].insert(1,candidato)
	return horario		

def Quitar (evento,*tempri):
	tempri=list(tempri)
	for idx,x in enumerate(tempri):
		if x[0]["nombre"]==evento:
			tempri.pop(idx)
	return tempri		

def Comprobar (seg,*horario, **candidato):
	for x in range(0,int(int(candidato["duracion"])/SEG_TEMP)+1):
		if horario[seg+x][1]!=None and not LOMASTARDE:
			return False
		elif LOMASTARDE and horario[seg-x][1]!=None:
			return False	
	return True

def Conflictos (horario, error):
	conflictos=[]
	for evento in error:
		return error					

Tempri=TablaTemPri(*IngresarEventos())
horario,error=BusquedaProfunda(*Tempri)
if LOMASTARDE:
	horario.reverse()
ImprimirDia(*horario)
error=Conflictos(horario,error)
print(error)


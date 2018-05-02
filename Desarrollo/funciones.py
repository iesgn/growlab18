from datetime import datetime, date, time, timedelta

SEG_TEMP=5 				# constante de tiempo (EN MINUTOS) para "segmentar" el dia
HORA = "%H:%M"			# Formato para la funcion datetime
FECHA= "%d/%m/%Y"
DESCANSO=0
FechaHoy=datetime.strptime("6/2/2018", FECHA)

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
			dic["fecha_inicio"]=datetime.strptime(evento.split(",")[4], FECHA)
			dic["fecha_fin"]=datetime.strptime(evento.split(",")[5], FECHA)
			dic["hora_inicio"]=datetime.strptime(evento.split(",")[6], HORA)
			if evento.split(",")[7] != "hora_fin":
				dic["hora_fin"]=datetime.strptime(evento.split(",")[7], HORA)
			else:
				dic["hora_fin"]=datetime.strptime(evento.split(",")[6], HORA)	# Si no tiene hora final, le asigno la hora 
				dic["hora_fin"]+=timedelta(minutes=(int(dic["duracion"])))			# inicial + duracion para que se genere solo un candidato
			dic["lomastarde"]=evento.split(",")[8]
			eventos.append(dic)														
	return eventos

def SelecEventos (*programa):
	entrada=[]
	for p in programa:
		if p["periodo"]=="F" and p["fecha_inicio"]==FechaHoy:
			entrada.append(p)
		elif p["periodo"]=="D" and (p["fecha_inicio"]<=FechaHoy and p["fecha_fin"]>=FechaHoy):
			entrada.append(p)
		elif p["periodo"]=="S" and (p["fecha_inicio"]<=FechaHoy and p["fecha_fin"]>=FechaHoy) and FechaHoy.weekday()==p["fecha_inicio"].weekday():
			entrada.append(p)
		elif p["periodo"]=="M" and (p["fecha_inicio"]<=FechaHoy and p["fecha_fin"]>=FechaHoy) and FechaHoy.day==p["fecha_inicio"].day:
			entrada.append(p)
	return entrada

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
			print("%s ==> -----"%x[0].strftime(HORA))
		elif x[1]=="Descanso":
			print("%s ==> Descanso"%x[0].strftime(HORA))
		else:	
			print("%s ==> %s"%(x[0].strftime(HORA),x[1]["nombre"]))

# Funcion para calcular el numero de candidatos de un evento | Retorna un entero			
def CalcularCandidatos(**kwargs):	
	candidatos = abs(((kwargs["hora_inicio"].hour*60) + kwargs["hora_inicio"].minute) - ((kwargs["hora_fin"].hour*60) + kwargs["hora_fin"].minute - int(kwargs["duracion"])))/SEG_TEMP
	return int(candidatos+1)		

# Rellena la lista con todos los candidatos ordenados por tiempo / prioridad | Retorna una lista de listas de diccionarios			
def TablaTemPri(*args):                                                                     
	tempri=[]
	priUno=[]
	priDos=[]
	priTres=[]
	for evento in args:
		if evento["prioridad"]=="1":
			priUno.append(evento)
		elif evento["prioridad"]=="2":
			priDos.append(evento)
		elif evento["prioridad"]=="3":
			priTres.append(evento)

	tempri.append(priTres)
	tempri.append(priDos)
	tempri.append(priUno)
	return tempri

def BuscarSeg(*horario,**candidato):
	for idx,x in enumerate(horario):
		if x[0]==candidato["hora_inicio"]:
			return idx

def Comprobar (seg,*horario, **candidato):
	tope=int(int(candidato["duracion"])/SEG_TEMP)+1+int(DESCANSO/SEG_TEMP)
	for x in range(0,tope):
		if horario[seg+x][1]!=None and horario[seg+x][1]!=candidato:
			return False
	return True

################################################################################################
#                                EN PRUEBA
################################################################################################

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
	
def BusquedaProfunda(*tempri):
	tempri=list(tempri)
	error=[]
	dia=GenerarTablaDia()
	horario=dia.copy()

	for x in range(0,3):
		while len(tempri[x])>0:
			candidato,estado,seg=SelecCandidato(horario,tempri[x])
			if estado:
				horario=Rellenar(seg,*horario,**candidato)	
			else:
				conflictos=Conflictos(horario,candidato)
				for idz,conflicto in enumerate(conflictos):
					if candidato["lomastarde"]:
						seg=conflicto[1]-1
					else:
						seg=conflicto[1]+1		
					if len(GenerarCandidatos(**conflicto[0]))>1 and Comprobar(seg,*horario,**conflicto[0]):
						Borrar(conflicto[1],*horario,**conflicto[0])
						Rellenar(seg,*horario,**conflicto[0]) 
						break
					if idz == len(conflictos)-1:
						for idu,u in enumerate(tempri[x]):
							if u in GenerarCandidatos(**candidato):
								print(idu)
								error.append(tempri[x].pop(idu))		
	return horario, error

def SelecCandidato (horario, tempri):
	for idx,bloque in enumerate(tempri):
		if len(GenerarCandidatos(**bloque))==1:
			seg=BuscarSeg(*horario,**bloque)
			return tempri.pop(idx), True, seg		
	for idy,evento in enumerate(tempri):
		candidatos=GenerarCandidatos(**evento)
		if candidatos[0]["lomastarde"]=="True":
			candidatos.reverse()
		for candidato in candidatos:
			seg=BuscarSeg(*horario,**candidato)
			if Comprobar(seg,*horario,**candidato):
				return tempri.pop(idy), True, seg
		return evento, False, seg

def Rellenar (seg,*horario,**candidato):
	horario=list(horario)
	tope=int(int(candidato["duracion"])/SEG_TEMP)+1+int(DESCANSO/SEG_TEMP)
	for x in range(0,tope):
		if x < tope-int(DESCANSO/SEG_TEMP):	
			horario[seg+x].insert(1,candidato)
		else:
			horario[seg+x].insert(1,"Descanso")	
	return horario		

def Borrar (seg,*horario,**candidato):
	horario=list(horario)
	tope=int(int(candidato["duracion"])/SEG_TEMP)+1+int(DESCANSO/SEG_TEMP)
	for x in range(0,tope):
		horario[seg+x].insert(1,None)
	return horario

def Conflictos (horario,evento):
	conflictos=[]
	segmentos=[]
	seg=BuscarSeg(*horario, **evento)
	fin=int(abs(((evento["hora_inicio"].hour*60) + evento["hora_inicio"].minute) - ((evento["hora_fin"].hour*60) + evento["hora_fin"].minute))/SEG_TEMP)
	for x in range(0,fin):
		if horario[seg+x][1]!=None and horario[seg+x][1] not in conflictos:
			conflictos.append(horario[seg+x][1])
			segmentos.append(seg+x)
	conflictos=list(zip(conflictos,segmentos))		
	return conflictos
			
eventos=SelecEventos(*IngresarEventos())
Tempri=TablaTemPri(*eventos)
horario,error=BusquedaProfunda(*Tempri)
ImprimirDia(*horario)
print(error)
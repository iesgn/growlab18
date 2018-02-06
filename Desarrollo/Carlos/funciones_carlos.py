SEG_TEMP=5 	# constante de tiempo (EN MINUTOS) para "segmentar" el dia

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
			dic["hora_inicio"]=evento.split(",")[6]
			dic["hora_fin"]=evento.split(",")[7].split("\n")
			eventos.append(dic)
	return eventos
# Genero la lista del tamano correspondiente a la constante 
def GenerarTablaDia():		
	dia=[]
	for x in range(int((60/SEG_TEMP)*24)):
		dia.append(None)
	return dia
# Funcion para imprimir la planificacion del dia	
def ImprimirDia(*args):
	hora,minuto=0,0
	for x in args:
		print("%.2i:%.2i ==> %s"%(hora,minuto,x))
		minuto+=SEG_TEMP
		if minuto==60:
			hora+=1
			minuto=0

dia=GenerarTablaDia()
ImprimirDia(*dia)


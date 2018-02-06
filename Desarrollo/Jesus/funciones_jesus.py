from datetime import timedelta
#Calcula los huecos que hay en un dia segun el intervalo indicado, representa cada hueco como *.
def calcular_huecos_dia(intervalo):
	lista = []
	for elem in range(int((60 / intervalo) * 24)):
		lista.append('*')
	return lista

#Programa un evento con las características indicadas.
def programar_evento(nombre, periodo, prioridad, duracion, fecha_inicio, hora_inicio, fecha_fin, hora_fin):
	lista = [{'nombre':nombre}, {'periodo':periodo}, {'prioridad':prioridad}, {'duracion':duracion}, {'fecha_inicio':fecha_inicio}, {'hora_inicio':hora_inicio}, 
	{'fecha_fin':fecha_fin}, {'hora_fin':hora_fin}]
	return lista

#Calcula el número de candidatos posibles entre dos horas con un intervalo determinado.
def calcular_candidatos(intervalo, hora_inicio, hora_fin):
	rango_horas = timedelta(hours=int(hora_inicio.split(':')[0]), minutes=int(hora_inicio.split(':')[1]))
	rango_horas_2 = timedelta(hours=int(hora_fin.split(':')[0]), minutes=int(hora_fin.split(':')[1]))
	diferencia = abs(rango_horas.total_seconds() - rango_horas_2.total_seconds())
	candidatos = diferencia / (intervalo * 60)
	return candidatos

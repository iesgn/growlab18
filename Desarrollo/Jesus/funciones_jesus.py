#Calcula los huecos que hay en un dia segun el intervalo indicado, representa cada hueco como *.
def calcular_huecos(intervalo):
	lista = []
	for elem in range(int((60 / intervalo) * 24)):
		lista.append('*')
	return lista

#Programa un evento con las características indicadas.
def programar_evento(nombre, periodo, prioridad, duracion, fecha_inicio, hora_inicio, fecha_fin, hora_fin):
	lista = [{'nombre':nombre}, {'periodo':periodo}, {'prioridad':prioridad}, {'duracion':duracion}, {'fecha_inicio':fecha_inicio}, {'hora_inicio':hora_inicio}, 
	{'fecha_fin':fecha_fin}, {'hora_fin':hora_fin}]
	return lista

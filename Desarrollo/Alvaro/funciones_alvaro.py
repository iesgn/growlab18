# Función que crea una lista con huecos (' ')

def crea_lista_huecos(intervalo):
	lista = []
	for i in range(24 * (60 // intervalo)):
		lista.append(' ')
	return lista

# Lista de diccionarios con la programación de eventos

def programacion_eventos(numero_eventos):
	lista = []
	for i in range(numero_eventos):
		evento = {}
		evento['codigo'] = input('Código: ')
		evento['nombre'] = input('Nombre: ')
		evento['periodo'] = input('Período: ')
		evento['duracion'] = input('Duración: ')
		evento['descripcion'] = input('Descripción: ')
		evento['prioridad'] = input('Prioridad: ')
		evento['fecha_inicio'] = input('Fecha inicio: ')
		evento['fecha_fin'] = input('Fecha fin: ')
		evento['hora_inicio'] = input('Hora inicio: ') 
		evento['hora_fin'] = input('Hora fin: ')
		lista.append(evento)
	return lista

# Calcular la lista de eventos candidatos

	# Quiero entender mejor las horas/fechas antes de hacer la función
#Calcula los huecos que hay en un dia segun el intervalo indicado, representa cada hueco como *.
def calcular_huecos(intervalo):
	lista = []
	for elem in range(int((60 / intervalo) * 24)):
		lista.append("*")
	return lista

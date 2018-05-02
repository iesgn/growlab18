import agenda
import datetime


def rango_fechas(desde, hasta):
    rango = []
    # Calculamos la diferencia de los días
    dias_totales = (hasta - desde).days
    for days in range(dias_totales + 1): 
        fecha = desde + datetime.timedelta(days=days)
        rango.append(fecha)
    return rango



def geteventos(finicio,ffinal):
	FI=datetime.datetime.strptime(finicio, "%Y-%m-%d")
	FF=datetime.datetime.strptime(ffinal, "%Y-%m-%d")	
	FI=datetime.datetime.strptime("2018-05-02", "%Y-%m-%d")	
	FF=datetime.datetime.strptime("2018-05-03", "%Y-%m-%d")
	horarios={}
	errores={}
	fechas = rango_fechas(FI,FF)
	for fecha in fechas:
		agenda.FechaHoy=fecha
		eventos=agenda.SelecEventos(*agenda.IngresarEventos())
		Tempri=agenda.TablaTemPri(*eventos)
		horario,error=agenda.BusquedaProfunda(*Tempri)
		horarios[fecha.strftime("%Y-%m-%d")]=horario	
		errores[fecha.strftime("%Y-%m-%d")]=error

	
	eventos=[]			#para que? Quieres esta lista para hacer la pagina eventos?
	for fecha,horario in horarios.items(): #que te da horarios.items()?
		for tiempo in horario:
			if tiempo[1] and tiempo[1] not in eventos: 
				eventos.append((tiempo[0],tiempo[1]["nombre"],fecha))
				print((tiempo[0],tiempo[1]["nombre"],fecha))	

	
	events=[]
	for fecha in fechas:
		for evento in set(list(e[1] for e in eventos if e[2]==fecha.strftime("%Y-%m-%d"))):
			new_event={}
			new_event["title"]=evento
			new_event["start"]= [e[2] for e in eventos if e[1]==evento and e[2]==fecha.strftime("%Y-%m-%d")][0]+"T"+[e[0] for e in eventos if e[1]==evento and e[2]==fecha.strftime("%Y-%m-%d")][0].strftime("%H:%M:%S")
			new_event["end"]= [e[2] for e in eventos if e[1]==evento and e[2]==fecha.strftime("%Y-%m-%d")][-1]+"T"+[e[0] for e in eventos if e[1]==evento and e[2]==fecha.strftime("%Y-%m-%d")][-1].strftime("%H:%M:%S")
			events.append(new_event)
	print(events)
	return events, errores
	



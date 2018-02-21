CREATE TABLE USUARIOS
(
Email 		VARCHAR() UNIQUE,
Usuario 	VARCHAR(10),
Password 	DATE,
PRIMARY KEY (Email)
);

CREATE TABLE INVITACIONES
(
Usuario_Email 	VARCHAR(),
Cod_Eventos 	INTEGER(),
PRIMARY KEY (Usuario_Email, Cod_Eventos),
FOREIGN KEY (Usuario_Email) REFERENCES USUARIOS (Email),
FOREIGN KEY (Cod_Eventos) 	REFERENCES EVENTOS (Codigo)
);

CREATE TABLE EVENTOS
(
Codigo 			INTEGER(),
Email 			VARCHAR(),
Titulo 			VARCHAR(),
Duracion		VARCHAR(),
Descripcion 	VARCHAR(),
Fecha[inicio]	INTEGER(),
Horario inicio 	INTEGER(),
Horario fin 	INTEGER(),
PRIMARY KEY (Codigo),
FOREIGN KEY (Email)	REFERENCES USUARIOS(Email)
);

CREATE TABLE EVENTOS_FUTUROS
(
Eventos_programacion	INTEGER(),
Fecha fin				INTEGER(),
PRIMARY KEY (Eventos_programacion),
FOREIGN KEY	(Eventos_programacion) REFERENCES EVENTOS(Codigo)
);

CREATE TABLE EVENTOS_PASADOS
(
Eventos_programacion	INTEGER(),
Hora inicio				INTEGER(),
Hora fin				INTEGER(),
Fecha					DATE,
PRIMARY KEY (Eventos_programacion),
FOREIGN KEY	(Eventos_programacion) REFERENCES EVENTOS(Codigo)
);

CREATE TABLE PERIODOS_EVENTOS
(
Periodos_codigo 		INTEGER(),
Eventos_programacion 	INTEGER(),
PRIMARY KEY (Periodos_codigo, Eventos_programacion),
FOREIGN KEY (Periodos_codigo)		REFERENCES PERIODOS (Codigo),
FOREIGN KEY (Eventos_programacion) 	REFERENCES EVENTOS (Codigo)
);

CREATE TABLE PRIORIDADES_EVENTOS
(
Prioridades_codigo 		INTEGER(),
Eventos_programacion 	INTEGER(),
PRIMARY KEY (Prioridades_codigo, Eventos_programacion),
FOREIGN KEY (Prioridades_codigo)	REFERENCES PRIORIDADES (Codigo),
FOREIGN KEY (Eventos_programacion) 	REFERENCES EVENTOS (Codigo)
);

CREATE TABLE PERIODOS
(
Codigo	INTEGER(),
Nombre	VARCHAR(),
PRIMARY KEY (Codigo)
);

CREATE TABLE PRIORIDADES
(
Codigo	INTEGER(),
Nivel	VARCHAR(),
PRIMARY KEY (Codigo)
);
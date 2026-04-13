Proceso Pregunta12
	Definir temperatura Como Real;
	Definir resultado Como Caracter;
	
	Leer temperatura;
	
	resultado <- "Clima ";
	
	Si temperatura < 10 Entonces
		resultado <- resultado + "Frio";
	SiNo
		Si temperatura < 16 Entonces
			resultado <- resultado + "Tempaldo";
		SiNo
			Si temperatura < 24 Entonces
				resultado <- resultado + "Calido";
			SiNo
				resultado <- resultado + "Tropcial";
			FinSi
		FinSi
	FinSi
	
	Escribir  resultado;
	
FinProceso

Proceso Pregunta9
	// Realizar un algoritmo que permita leer dos valores, determinar cual de los dos valores es el menor y escríbalo
	Definir  comision, venta Como Entero;
	Leer venta;
	
	Si venta < 100 Entonces
		Escribir  "No hay comision";
		comision <- 0;
	SiNo
		Si venta < 300 Entonces
			Escribir  "Comision del 10%";
			comision <- venta * 0.1;
		SiNo
			Escribir  "Comision del 20%";
			comision <- venta * 0.2;
		FinSi
	FinSi
	
	Escribir "Comision: ", comision;
	
FinProceso

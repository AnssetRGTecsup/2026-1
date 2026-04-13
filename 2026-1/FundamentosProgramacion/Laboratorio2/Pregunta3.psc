Proceso Pregunta3
	// Realizar un algoritmo que permita leer dos valores, determinar cual de los dos valores es el menor y escríbalo
	Definir  numero1, numero2 Como Real;
	Leer numero1, numero2;
	
	Si numero1 < numero2 Entonces
		Escribir  "El menor numero es: ", numero1;
	SiNo
		Si numero2 < numero1 Entonces
			Escribir  "El menor numero es: ", numero2;	
		SiNo
			Escribir  "Ambos numeros son iguales";
		FinSi
	FinSi
	
FinProceso

Proceso Pregunta4
	// Realizar un algoritmo que permita leer dos valores, determinar cual de los dos valores es el menor y escríbalo
	Definir  num1, num2 Como Entero;
	Leer num1, num2;
	
	Definir operador Como Caracter;
	Leer operador;
	
	Si operador = 'S' Entonces
		Escribir "Suma: ", num1 + num2;
	FinSi
	
	Si operador = 'R' Entonces
		Escribir "Resta: ", num1 - num2;
	FinSi
	
	Si operador = 'M' Entonces
		Escribir "Multiplicar: ", num1 * num2;
	FinSi
	
	Si operador = 'D' Entonces
		
		Si num2 = 0 Entonces
			Escribir "No se puede divir entre cero";
		SiNo
			Escribir "Dividir: ", num1 / num2;
		FinSi
	FinSi
	
FinProceso

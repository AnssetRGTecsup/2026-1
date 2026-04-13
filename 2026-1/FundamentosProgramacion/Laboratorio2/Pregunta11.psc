Proceso Pregunta11
	Definir num1, num2, cubo, cuarta Como Real;
	
	Leer num1, num2;
	
	Si num1 <= 0 Entonces
		Escribir "El primer numero es negativo. No se acepta numeros negativos.";
	SiNo
		Si num2 <= 0 Entonces
			Escribir "El segundo numero es negativo. No se acepta numeros negativos.";
		SiNo
			Escribir "Los resultados del primer numero son: ", (num1^3), " y ", (num1^4);
			Escribir "Los resultados del segundo numero son: ", (num2^3), " y ", (num2^4);
		FinSi
	FinSi
	
FinProceso

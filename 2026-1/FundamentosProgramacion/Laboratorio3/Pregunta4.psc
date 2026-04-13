Proceso Pregunta4
	Definir n0, n1, n2, n, i Como Entero;
	n0 = 0;
	n1 = 1;
	i = 0;
	
	Escribir "Deterinar la cantidad de numeros";
	
	Leer n;
	
	Escribir n0;
	Escribir n1;
	
	Mientras i < n Hacer
		n2 = n1 + n0;
		n0 = n1;
		n1 = n2;
		
		Escribir n2;
		
		i = i +1;
	FinMientras
	
FinProceso

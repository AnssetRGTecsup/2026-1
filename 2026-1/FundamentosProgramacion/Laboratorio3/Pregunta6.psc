Proceso Pregunta6
	Definir n_impar, n_par, n, i Como Entero;
	
	n_impar  = 0;
	n_par  = 0;
	
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Leer n;
		
		Si n % 2 = 0 Entonces
			n_par = n_par + n;
		SiNo
			n_impar = n_impar + n;
		FinSi
	FinPara
	
	Escribir "Suma pares: ", n_par;
	Escribir "Suma impares: ", n_impar;
	
FinProceso

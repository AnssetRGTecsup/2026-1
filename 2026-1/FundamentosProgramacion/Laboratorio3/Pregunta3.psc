Proceso Pregunta3
	Definir num Como Real;
	Definir i, n_par, n_impar Como Entero;
	n_par <-0;
	n_impar <-0;
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Leer num;
		
		Si num % 2 = 0 Entonces
			n_par <- n_par + 1;
		SiNo
			n_impar <- n_impar + 1;
		FinSi
		
	FinPara
	
	Escribir n_par;
	Escribir n_impar;
FinProceso

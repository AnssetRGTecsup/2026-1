Proceso Pregunta7
	Definir  n_pos, n_neg, n_neutro, n, i, cantidad Como Entero;
	
	n_pos  = 0;
	n_neg = 0;
	n_neutro = 0;
	
	Escribir "Cantidad de numeros: ";
	Leer cantidad;
	
	Para i<-1 Hasta cantidad Con Paso 1 Hacer
		Leer n;
		
		Si n = 0 Entonces
			n_neutro = n_neutro + n;
		SiNo
			Si n > 0 Entonces
				n_pos = n_pos + n;
			SiNo
				n_neg = n_neg + n;
			FinSi
		FinSi
	FinPara
	
	Escribir "Numeros positivos: ", n_pos;
	Escribir "Numeros negativos: ", n_neg;
	Escribir "Numeros neutros: ", n_neutro;
	
FinProceso

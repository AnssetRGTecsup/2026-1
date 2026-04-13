Proceso Pregunta5
	Definir n_impar, n_par, n_pos, n_neg, n_neutro, n, i Como Entero;
	
	n_impar  = 0;
	n_par  = 0;
	n_pos  = 0;
	n_neg = 0;
	n_neutro = 0;
	
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Leer n;
		
		Si n % 2 = 0 Entonces
			n_par = n_par + 1;
		SiNo
			n_impar = n_impar + 1;
		FinSi
		
		Si n = 0 Entonces
			n_neutro = n_neutro + 1;
		SiNo
			Si n > 0 Entonces
				n_pos = n_pos + 1;
			SiNo
				n_neg = n_neg + 1;
			FinSi
		FinSi
	FinPara
	
	Escribir "Numeros pares: ", n_par;
	Escribir "Numeros impares: ", n_impar;
	Escribir "Numeros positivos: ", n_pos;
	Escribir "Numeros negativos: ", n_neg;
	Escribir "Numeros neutros: ", n_neutro;
	
FinProceso

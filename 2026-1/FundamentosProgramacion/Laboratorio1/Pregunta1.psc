Proceso Ejercicio1
	// Definición de variables
    Definir cateto1, cateto2, hipo Como Real;
    
    Escribir "Ingrese el valor del primer cateto:";
    Leer cateto1;
    Escribir "Ingrese el valor del segundo cateto:";
    Leer cateto2;
    
    // Proceso: Raíz cuadrada de la suma de los cuadrados
    hipo <- raiz(cateto1^2 + cateto2^2);
    
    Escribir "La hipotenusa es: ", hipo;
FinProceso

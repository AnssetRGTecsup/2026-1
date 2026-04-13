Proceso Ejercicio1
	Definir sueldo, tasaInteres, gananciaMensual, gananciaTotal, montoTotal Como Real;
    
    Escribir "Ingrese su sueldo:";
    Leer sueldo;
    Escribir "Ingrese la tasa de interés mensual (ejemplo: 2 para 2%):";
    Leer tasaInteres;
	
    // Calculamos la ganancia mensual basada en el interés ingresado
    montoTotal <- sueldo * ( 1 + tasaInteres / 100)^5;
    
    Escribir "Monto total tras 5 meses: ", montoTotal;
FinProceso

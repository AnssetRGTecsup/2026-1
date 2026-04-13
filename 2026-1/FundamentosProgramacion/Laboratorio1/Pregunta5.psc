Proceso Ejercicio1
	Definir sueldo, tasaInteres, gananciaMensual, montoTotal Como Real;
    
    Escribir "Ingrese su sueldo:";
    Leer sueldo;
    Escribir "Ingrese la tasa de interés mensual (ejemplo: 2 para 2%):";
    Leer tasaInteres;
	
    // Calculamos la ganancia mensual basada en el interés ingresado
    gananciaMensual <- sueldo * (tasaInteres / 100);
    // El monto total es el capital inicial más las ganancias de 5 meses
    montoTotal <- sueldo + (gananciaMensual * 5);
    
    Escribir "Ganancia por mes: ", gananciaMensual;
    Escribir "Monto total tras 5 meses: ", montoTotal;
FinProceso

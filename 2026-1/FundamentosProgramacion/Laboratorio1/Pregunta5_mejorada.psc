Proceso Ejercicio1
	Definir sueldo, tasaInteres, gananciaMensual, gananciaTotal, montoTotal Como Real;
    
    Escribir "Ingrese su sueldo:";
    Leer sueldo;
    Escribir "Ingrese la tasa de interés mensual (ejemplo: 2 para 2%):";
    Leer tasaInteres;
	
    // Calculamos la ganancia mensual basada en el interés ingresado
    gananciaMensual <- sueldo * (tasaInteres / 100);
    // El monto total es el capital inicial más las ganancia del monto o sueldo
    montoTotal <- sueldo + gananciaMensual;
	// Aumentamos la ganancia acumulada
	gananciaTotal <- gananciaMensual;
	
	// Mes 2
	// Calculamos la ganancia mensual basada en el interés ingresado
    gananciaMensual <- montoTotal * (tasaInteres / 100);
    // El monto total es el capital inicial más las ganancias de 5 meses
    montoTotal <- montoTotal + gananciaMensual;
	// Aumentamos la ganancia acumulada
	gananciaTotal <- gananciaTotal + gananciaMensual;
	
	// Mes 3
	// Calculamos la ganancia mensual basada en el interés ingresado
    gananciaMensual <- montoTotal * (tasaInteres / 100);
    // El monto total es el capital inicial más las ganancias de 5 meses
    montoTotal <- montoTotal + gananciaMensual;
	// Aumentamos la ganancia acumulada
	gananciaTotal <- gananciaTotal + gananciaMensual;
	
	// Mes 4
	// Calculamos la ganancia mensual basada en el interés ingresado
    gananciaMensual <- montoTotal * (tasaInteres / 100);
    // El monto total es el capital inicial más las ganancias de 5 meses
    montoTotal <- montoTotal + gananciaMensual;
	// Aumentamos la ganancia acumulada
	gananciaTotal <- gananciaTotal + gananciaMensual;
	
	// Mes 5
	// Calculamos la ganancia mensual basada en el interés ingresado
    gananciaMensual <- montoTotal * (tasaInteres / 100);
    // El monto total es el capital inicial más las ganancias de 5 meses
    montoTotal <- montoTotal + gananciaMensual;
	// Aumentamos la ganancia acumulada
	gananciaTotal <- gananciaTotal + gananciaMensual;
    
    Escribir "Ganancia total: ", gananciaTotal;
    Escribir "Monto total tras 5 meses: ", montoTotal;
FinProceso

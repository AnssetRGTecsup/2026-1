Proceso Ejercicio1
	// Definición de variables de entrada y salida
    Definir notaTeoria, notaPractica, notaExamen, promedio Como Real;
    
    // Entrada de datos
    Escribir "Ingrese la nota de Teoría (30%):";
    Leer notaTeoria;
    Escribir "Ingrese la nota de Práctica (40%):";
    Leer notaPractica;
    Escribir "Ingrese la nota del Examen Final (30%):";
    Leer notaExamen;
    
    // Proceso: Cálculo usando pesos decimales (30% = 0.3)
    promedio <- (notaTeoria * 0.30) + (notaPractica * 0.40) + (notaExamen * 0.30);
    
    // Salida de resultados
    Escribir "El promedio final es: ", promedio;
FinProceso

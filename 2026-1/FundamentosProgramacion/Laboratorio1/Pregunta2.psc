Proceso Ejercicio1
	Definir radio, area Como Real;
    
    Escribir "Ingrese el radio del círculo:";
    Leer radio;
    
    // Validación simple con condicional
    Si radio > 0 Entonces
        area <- PI * (radio^2);
        Escribir "El área del círculo es: ", area;
    Sino
        Escribir "Error: El radio debe ser mayor a cero.";
    FinSi
FinProceso

Proceso Ejercicio1
	Definir montoInicial, descuento, montoFinal Como Real;
    
    Escribir "Ingrese el monto total de la compra:";
    Leer montoInicial;
    
    descuento <- montoInicial * 0.15;
    montoFinal <- montoInicial - descuento;
    
    Escribir "Descuento aplicado: ", descuento;
    Escribir "Total a pagar: ", montoFinal;
FinProceso

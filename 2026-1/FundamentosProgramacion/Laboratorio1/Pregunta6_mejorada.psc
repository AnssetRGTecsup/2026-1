Proceso Ejercicio1
	Definir montoInicial, descuento, montoFinal Como Real;
    
    Escribir "Ingrese el monto total de la compra:";
    Leer montoInicial;
    
	Escribir "Se le aplicara un descuento base de 15%, en caso que su compra sea mayor a 15000 tendra un adicional del 20%";
	
	Si montoInicial > 15000 Entonces
		descuento <- montoInicial * 0.15 * 1.2;
	SiNo
		descuento <- montoInicial * 0.15;
	FinSi
	
    montoFinal <- montoInicial - descuento;
    
    Escribir "Descuento aplicado: ", descuento;
    Escribir "Total a pagar: ", montoFinal;
FinProceso

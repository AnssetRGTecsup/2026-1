monto = float(input("Ingrese el monto de compra: "))

descuento = monto * 0.8 if monto > 1000 else monto;

print(f"El monto a pagar es de S/.{monto}")
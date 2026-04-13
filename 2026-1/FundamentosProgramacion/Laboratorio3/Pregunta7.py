pares = 0
impares = 0
positivos = 0
negativos = 0
neutros = 0

n = int(input(f"Ingrese la cantidad de numeros: "))

for i in range(n):
    numero = int(input(f"Ingrese el número {i+1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero == 0:
        neutros += 1
    elif numero > 0:
        positivos += 1
    else:
        negativos += 1

print("Cantidad de Pares:", pares)
print("Cantidad de Impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
print("Cantidad de neutros:", neutros)
pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    
    if numero % 2 == 0:
        pares += numero
    else:
        impares += numero

print("La suma total es:", suma)
print("La suma total es:", suma / 10)
n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

if n1 == n2:
    print("Son iguales")
elif n1 > n2:
    print(f"{n1} es el mayor")
else:
    print(f"{n2} es el mayor")
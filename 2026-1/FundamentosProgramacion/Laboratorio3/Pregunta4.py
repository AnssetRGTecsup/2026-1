n0 = 0
n1 = 1

n = int(input(f"Ingrese el numero de fibonaccis a mostrar"))

for i in range(n):
    n2 = n1 + n0
    n0 = n1
    n1 = n2
    
    print(f"N° {i}: {n2}")
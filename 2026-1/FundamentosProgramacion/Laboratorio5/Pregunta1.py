valido = False # Variable que nos dirá si encontramos un número válido o no

while valido == False:
    entrada = input("Ingrese un número entero: ") # Leemos el input como un valor string

    print(type(entrada))

    print(entrada)
    # lstrip('-') -> en caso de existir un "-" lo eliminamos de la cadena
    print(entrada.lstrip('-'))

    # lstrip('-') -> en caso de existir un "-" lo eliminamos de la cadena
    print(entrada.lstrip('-').isdigit())
    
    if entrada.lstrip('-').isdigit():
        # En caso de ser un número, lo transformamos a tipo de número entero
        numero = int(entrada)
        valido = True
    else:
        # En caso de ser diferente a un número, continuamos en el loop
        print("Error: debe ingresar un número válido")

# Verificar si es par o impar
if numero % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")
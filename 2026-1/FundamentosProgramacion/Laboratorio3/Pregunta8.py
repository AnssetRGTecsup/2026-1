def loop_simple_for():
    for i in range(101):
        print(i)

def loop_custom_for():
    for i in range(0, 101):
        print(i)

def loop_while():
    i = 0
    while i < 101:
        print(i)
        i += 1

def loop_simple_for():
    for i in range(101):
        print(i)

def loop_custom_for():
    for i in range(0, 101):
        print(i)

def loop_while():
    i = 0
    while i < 101:
        print(i)
        i += 1

def main():
    print("Seleccione una opción:")
    print("1. Simple For")
    print("2. Custom For")
    print("3. While")

    opcion = input("Ingrese una opción (1-3): ")

    match opcion:
        case "1":
            loop_simple_for()
        case "2":
            loop_custom_for()
        case "3":
            loop_while()
        case _:
            print("Opción no válida")

if __name__ == "__main__":
    main()
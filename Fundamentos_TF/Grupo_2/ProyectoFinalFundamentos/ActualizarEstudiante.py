from constantes import EST_NOMBRE, EST_CICLO

def ActualizarEstudiante(estudiante):
    print("\n--- ACTUALIZAR DATOS DEL ESTUDIANTE ---")
    if not estudiante:
        print("No hay ningún estudiante registrado en el sistema.")
        return

    print("¿Qué dato desea modificar?")
    print("1. Nombre completo")
    print("2. Ciclo actual")
    opc = input("Seleccione una opción: ").strip()

    if opc == "1":
        estudiante[EST_NOMBRE] = input("Ingrese el nuevo nombre completo: ").strip()
        print("\n¡Nombre actualizado con éxito!")
    elif opc == "2":
        while True:
            try:
                nuevo_ciclo = int(input("Ingrese el nuevo ciclo actual: "))
                if nuevo_ciclo > 0:
                    estudiante[EST_CICLO] = nuevo_ciclo
                    break
                print("El ciclo debe ser mayor a 0.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")
        print("\n¡Ciclo actualizado con éxito!")
    else:
        print("Opción no válida. Operación cancelada.")
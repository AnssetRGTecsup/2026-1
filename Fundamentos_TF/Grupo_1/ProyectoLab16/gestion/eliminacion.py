def eliminar_cursos(estudiante):
    if estudiante is None or not estudiante.tiene_cursos():
        print("\nNo hay cursos registrados.\n")
        return

    print("\n Eliminar Curso(s) ")
    print("1. Eliminar un curso")
    print("2. Eliminar varios cursos")
    print("3. Eliminar todos los cursos")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre = input("Nombre del curso a eliminar: ")
        curso = estudiante.buscar_curso(nombre)

        if curso is not None:
            estudiante.eliminar_curso(curso)
            print("Curso eliminado correctamente.\n")
        else:
            print("Curso no encontrado.\n")

    elif opcion == "2":
        nombres = input("Nombres de los cursos separados por coma: ")
        lista_nombres = nombres.split(",")
        for nombre in lista_nombres:
            nombre = nombre.strip()
            curso = estudiante.buscar_curso(nombre)

            if curso is not None:
                estudiante.eliminar_curso(curso)
                print("Curso '" + nombre + "' eliminado.")
            else:
                print("Curso '" + nombre + "' no encontrado.")
        print()

    elif opcion == "3":
        confirmar = input("¿Seguro que desea eliminar todos los cursos? (s/n): ")
        if confirmar.lower() == "s":
            estudiante.cursos = []
            print("Todos los cursos han sido eliminados.\n")
        else:
            print("Operación cancelada.\n")

    else:
        print("Opción inválida.\n")

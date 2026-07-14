from constantes import EST_CURSOS

def EliminarCurso(estudiante):
    print("\n--- ELIMINAR CURSO(S) ---")
    if not estudiante or not estudiante[EST_CURSOS]:
        print("No hay cursos registrados para eliminar.")
        return

    print("¿Qué desea hacer?")
    print("1. Eliminar solo 1 curso")
    print("2. Eliminar varios cursos a la vez")
    print("3. Eliminar TODOS los cursos")
    opc = input("Seleccione una opción: ").strip()

    if opc == "1":
        nombre = input("Ingrese el nombre del curso a eliminar: ").strip()
        curso_llave = None
        
        for curso in estudiante[EST_CURSOS]:
            if curso.lower() == nombre.lower():
                curso_llave = curso
                break
                
        if curso_llave:
            del estudiante[EST_CURSOS][curso_llave]
            print(f"Curso '{curso_llave}' eliminado con éxito.")
        else:
            print(f"El curso '{nombre}' no fue encontrado.")

    elif opc == "2":
        print("Ingrese los nombres de los cursos separados por comas (ejm: Matemática, Física):")
        lista_nombres = input("Cursos a eliminar: ").split(",")
        eliminados = []
        
        for nombre_crudo in lista_nombres:
            nombre_limpio = nombre_crudo.strip().lower()
            curso_llave = None
            for curso in estudiante[EST_CURSOS]:
                if curso.lower() == nombre_limpio:
                    curso_llave = curso
                    break
            if curso_llave:
                eliminados.append(curso_llave)
                del estudiante[EST_CURSOS][curso_llave]
                    
        if eliminados:
            print(f"\n¡Se eliminaron con éxito los siguientes cursos: {', '.join(eliminados)}!")
        else:
            print("\nNo se encontró ninguno de los cursos especificados.")

    elif opc == "3":
        confirmar = input("¿Está seguro de eliminar TODOS los cursos del estudiante? (S/N): ").strip().upper()
        if confirmar == "S":
            estudiante[EST_CURSOS].clear()
            print("Todos los cursos han sido borrados de la lista.")
        else:
            print("Operación cancelada.")
    else:
        print("Opción no válida. Operación cancelada.")
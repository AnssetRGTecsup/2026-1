from constantes import EST_CURSOS, CUR_HORAS

def ActualizarHoras(estudiante):
    print("\n--- ACTUALIZAR HORAS DE ESTUDIO ---")
    if not estudiante or not estudiante[EST_CURSOS]:
        print("No hay cursos registrados para este estudiante.")
        return

    nombre_input = input("Ingrese el nombre del curso para registrar horas: ").strip()
    curso_llave = None

    
    for curso in estudiante[EST_CURSOS]:
        if curso.lower() == nombre_input.lower():
            curso_llave = curso
            break

    if not curso_llave:
        print(f"El curso '{nombre_input}' no existe.")
        return

    while True:
        try:
            horas = float(input(f"Ingrese las horas de estudio dedicadas hoy a {curso_llave}: "))
            if horas >= 0:
                break
            print("Las horas no pueden ser negativas.")
        except ValueError:
            print("Entrada inválida. Ingrese un valor numérico.")

    
    estudiante[EST_CURSOS][curso_llave][CUR_HORAS].append(horas)
    print(f"\n¡Se han registrado {horas} horas de estudio para el curso {curso_llave}!")
from constantes import EST_CURSOS, CUR_CREDITOS, CUR_EVALUACIONES, CUR_HORAS

def RegistrarCurso(estudiante):
    print("\n--- REGISTRAR NUEVO CURSO ---")
    if not estudiante:
        print("Primero debe registrar un estudiante en el sistema.")
        return

    nombre_curso = input("Ingrese el nombre del curso: ").strip()
    
    
    if nombre_curso.lower() in [c.lower() for c in estudiante[EST_CURSOS]]:
        print(f"El curso '{nombre_curso}' ya se encuentra registrado.")
        return

    while True:
        try:
            creditos = int(input("Ingrese los créditos del curso: "))
            if creditos > 0:
                break
            print("Los créditos deben ser mayores a 0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    
    estudiante[EST_CURSOS][nombre_curso] = {
        CUR_CREDITOS: creditos,
        CUR_EVALUACIONES: [],   
        CUR_HORAS: [],           
    }

    print(f"\n¡Curso '{nombre_curso}' registrado con éxito!")
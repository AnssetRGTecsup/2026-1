from constantes import EST_CURSOS, CUR_EVALUACIONES, EVA_NOMBRE, EVA_FECHA, EVA_NOTA, EVA_PESO
from ConvertirFecha import ConvertirFecha

def ActualizarEvaluaciones(estudiante):
    print("\n--- ACTUALIZAR EVALUACIONES DE UN CURSO ---")
    if not estudiante or not estudiante[EST_CURSOS]:
        print("No hay cursos registrados para este estudiante.")
        return

    nombre_input = input("Ingrese el nombre del curso a modificar: ").strip()
    curso_llave = None

   
    for curso in estudiante[EST_CURSOS]:
        if curso.lower() == nombre_input.lower():
            curso_llave = curso
            break

    if not curso_llave:
        print(f"El curso '{nombre_input}' no existe.")
        return

    print(f"\nCurso seleccionado: {curso_llave}")
    nombre_evaluacion = input("Ingrese el nombre de la evaluación (ejm: PC1, PC2, EA, EB): ").strip()

    fecha = ConvertirFecha(input("Ingrese la fecha de la evaluación (dd/mm/aaaa): "))
    while fecha is None:
        print("Fecha inválida.")
        fecha = ConvertirFecha(input("Ingrese la fecha de la evaluación (dd/mm/aaaa): "))

    while True:
        try:
            nota = float(input("Ingrese la nota obtenida (0 a 20): "))
            if 0 <= nota <= 20:
                break
            print("La nota debe estar en el rango de 0 a 20.")
        except ValueError:
            print("Entrada inválida. Ingrese un número decimal o entero.")

    while True:
        try:
            peso = float(input("Ingrese el peso de la evaluación (ejm: 0.20 para el 20%): "))
            if 0 < peso <= 1:
                break
            print("El peso debe ser mayor a 0 y menor o igual a 1.")
        except ValueError:
            print("Entrada inválida. Ingrese un número decimal.")

    
    nueva_evaluacion = {
        EVA_NOMBRE: nombre_evaluacion,
        EVA_FECHA: fecha,
        EVA_NOTA: nota,
        EVA_PESO: peso
    }

    
    estudiante[EST_CURSOS][curso_llave][CUR_EVALUACIONES].append(nueva_evaluacion)

    print(f"\n¡Evaluación '{nombre_evaluacion}' guardada con éxito en {curso_llave}!")
from modelos.entidades import Evaluacion, HabitoEstudio
from utilidades.validaciones import leer_flotante, leer_fecha


def actualizar_datos_estudiante(estudiante):
    if not estudiante:
        print("\nPrimero debe registrar al estudiante.\n")
        return

    print("\nActualizar Datos del Estudiante")
    print("Deje en blanco si no desea cambiar el dato.")

    nombre = input(f"Nuevo nombre ({estudiante.nombre}): ").strip()
    codigo = input(f"Nuevo código ({estudiante.codigo}): ").strip()
    ciclo_input = input(f"Nuevo ciclo ({estudiante.ciclo}): ").strip()

    if nombre:
        estudiante.nombre = nombre
    if codigo:
        estudiante.codigo = codigo
    if ciclo_input:
        try:
            estudiante.ciclo = int(ciclo_input)
        except ValueError:
            print("Ciclo inválido. No se realizó el cambio.")

    print("Datos actualizados correctamente.\n")


def actualizar_evaluaciones(estudiante):
    if not estudiante or not estudiante.tiene_cursos():
        print("\nNo hay cursos registrados.\n")
        return

    print("\nActualizar Evaluaciones")
    nombre_curso = input("Nombre del curso: ")
    curso = estudiante.buscar_curso(nombre_curso)

    if not curso:
        print("Curso no encontrado.\n")
        return

    nombre_eval = input("Nombre de la evaluación (Ej: PA, EX, PR): ").strip()

    valido_nota, nota = leer_flotante("Nota (0 a 20): ")
    valido_peso, peso = leer_flotante("Peso (Ej: 0.20 para 20%): ")
    valido_fecha, fecha = leer_fecha("Fecha de la evaluación (dd/mm/aaaa): ")

    if not valido_nota or not valido_peso:
        print("Error: la nota y el peso deben ser valores numéricos. Operación cancelada.\n")
        return

    if not valido_fecha:
        print("Error: la fecha debe tener el formato dd/mm/aaaa. Operación cancelada.\n")
        return

    curso.agregar_evaluacion(Evaluacion(nombre_eval, fecha, nota, peso))
    print("Evaluación registrada correctamente.\n")


def actualizar_horas_estudio(estudiante):
    if not estudiante or not estudiante.tiene_cursos():
        print("\nNo hay cursos registrados.\n")
        return

    print("\nActualizar Horas de Estudio")
    nombre_curso = input("Nombre del curso: ")
    curso = estudiante.buscar_curso(nombre_curso)

    if not curso:
        print("Curso no encontrado.\n")
        return

    valido_horas, horas = leer_flotante("Horas dedicadas al curso: ")
    if not valido_horas:
        print("Error: las horas deben ser un número válido. Operación cancelada.\n")
        return

    valido_fecha, fecha = leer_fecha("Fecha en que estudió (dd/mm/aaaa): ")
    if not valido_fecha:
        print("Error: la fecha debe tener el formato dd/mm/aaaa. Operación cancelada.\n")
        return

    curso.agregar_habito_estudio(HabitoEstudio(fecha, horas))
    print("Horas registradas correctamente.\n")

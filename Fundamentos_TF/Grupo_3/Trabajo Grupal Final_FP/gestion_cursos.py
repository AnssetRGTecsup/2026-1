"""Funciones para la gestión de cursos del estudiante activo."""

from modelos import Curso
from utils import confirmar, leer_creditos, leer_entero, leer_texto, mostrar_contexto, seleccionar_varios


def registrar_curso(sistema):
    """Registra uno o varios cursos para el estudiante activo."""
    estudiante = sistema.estudiante_activo
    mostrar_contexto(estudiante)

    cantidad = leer_entero("¿Cuántos cursos va a registrar?: ")

    for numero in range(1, cantidad + 1):
        print(f"\n--- Curso {numero} de {cantidad} ---")
        nombre = leer_texto("Nombre del curso: ")

        if estudiante.existe_curso(nombre):
            print("Error: ese curso ya está registrado. Se omite.")
            continue

        creditos = leer_creditos("Créditos: ")
        estudiante.agregar_curso(Curso(nombre, creditos))

    print(f"\n{cantidad} curso(s) procesado(s) correctamente.")


def eliminar_cursos(sistema):
    
    estudiante = sistema.estudiante_activo
    mostrar_contexto(estudiante)

    cursos = seleccionar_varios(estudiante.cursos, "curso")

    if not cursos:
        return

    nombres = ", ".join(curso.nombre for curso in cursos)
    if not confirmar(f"¿Seguro que desea eliminar: {nombres}?"):
        print("Operación cancelada.")
        return

    for curso in cursos:
        estudiante.eliminar_curso(curso)

    print(f"{len(cursos)} curso(s) eliminado(s) correctamente.")


def consultar_cursos(sistema):
   
    estudiante = sistema.estudiante_activo
    mostrar_contexto(estudiante)

    cursos = seleccionar_varios(estudiante.cursos, "curso")

    for curso in cursos:
        print(f"\nCurso: {curso.nombre}")
        print(f"Créditos: {curso.creditos}")
        print(f"Promedio: {curso.promedio():.2f}")
        print(f"Total de horas de estudio: {curso.total_horas():.2f}")

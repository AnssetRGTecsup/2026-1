from modelos.entidades import Estudiante, Curso
from utilidades.validaciones import leer_entero


def registrar_estudiante():
    print("\nRegistrar Estudiante")
    nombre = input("Nombre del estudiante: ").strip()
    codigo = input("Código del estudiante: ").strip()

    valido, ciclo = leer_entero("Ciclo: ")
    if not valido:
        print("Ciclo inválido, debe ser un número entero. Operación cancelada.\n")
        return None

    estudiante = Estudiante(nombre, codigo, ciclo)
    print("Estudiante registrado correctamente.\n")
    return estudiante


def registrar_curso(estudiante):
    if estudiante is None:
        print("\nPrimero debe registrar al estudiante.\n")
        return

    print("\nRegistrar curso")
    nombre_buscar = input("Nombre del curso: ").strip()

    if estudiante.buscar_curso(nombre_buscar) is not None:
        print("Ese curso ya existe.\n")
        return

    valido, creditos = leer_entero("Créditos: ")
    if not valido:
        print("Créditos inválidos, debe ser un número entero. Operación cancelada.\n")
        return

    nuevo_curso = Curso(nombre_buscar, creditos)
    estudiante.agregar_curso(nuevo_curso)
    print("Curso registrado correctamente.\n")

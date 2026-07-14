from modelos import Estudiante
from utils import confirmar, leer_entero, leer_nombre, leer_texto, seleccionar_uno


def registrar_estudiante(sistema):

    print("\n--- Registrar Estudiante ---")
    nombre = leer_nombre("Nombre: ")
    codigo = leer_texto("Código: ")

    if sistema.existe_codigo(codigo):
        print("Error: el código ya está registrado.")
        return

    ciclo = leer_entero("Ciclo: ")
    estudiante = Estudiante(nombre, codigo, ciclo)
    sistema.agregar_estudiante(estudiante)
    print(f"Estudiante {nombre} registrado y activado correctamente.")


def actualizar_estudiante(sistema):

    estudiante = sistema.estudiante_activo

    print("\n--- Actualizar Estudiante ---")
    print(f"1. Nombre actual: {estudiante.nombre}")
    print(f"2. Ciclo actual: {estudiante.ciclo}")
    opcion = leer_entero("¿Qué desea actualizar? (1/2): ")

    if opcion == 1:
        estudiante.nombre = leer_nombre("Nuevo nombre: ")
    elif opcion == 2:
        estudiante.ciclo = leer_entero("Nuevo ciclo: ")
    else:
        print("Opción inválida.")
        return

    print("Datos actualizados correctamente.")


def cambiar_estudiante_activo(sistema):
    """ Permite elegir estudiante activo """
    if len(sistema.estudiantes) == 1:
        estudiante = sistema.estudiantes[0]
        sistema.estudiante_activo = estudiante
        print(f"Ya está activo {estudiante.nombre}, es el único estudiante registrado.")
        return

    estudiante = seleccionar_uno(sistema.estudiantes, "estudiante")

    if estudiante:
        sistema.estudiante_activo = estudiante
        print(f"Estudiante activo: {estudiante.nombre}")


def eliminar_estudiante(sistema):

    estudiante = seleccionar_uno(sistema.estudiantes, "estudiante")

    if estudiante is None:
        return

    if confirmar(f"¿Seguro que desea eliminar a {estudiante.nombre}?"):
        sistema.eliminar_estudiante(estudiante)
        print("Estudiante eliminado correctamente.")


def mostrar_estudiantes(sistema):
   
    if not sistema.estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("\n===== ESTUDIANTES REGISTRADOS =====")
    for estudiante in sistema.estudiantes:
        activo = " (Activo)" if estudiante == sistema.estudiante_activo else ""
        print(
            f"Código: {estudiante.codigo} | Nombre: {estudiante.nombre} | "
            f"Ciclo: {estudiante.ciclo}{activo}"
        )

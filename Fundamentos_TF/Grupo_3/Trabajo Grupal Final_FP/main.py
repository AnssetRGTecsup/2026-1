from gestion_cursos import consultar_cursos, eliminar_cursos, registrar_curso
from gestion_estudiante import (
    actualizar_estudiante,
    cambiar_estudiante_activo,
    eliminar_estudiante,
    mostrar_estudiantes,
    registrar_estudiante,
)
from gestion_evaluaciones import actualizar_evaluacion, registrar_evaluacion
from gestion_horas import actualizar_horas, registrar_horas
from graficos import (
    generar_grafico_evolucion,
    generar_grafico_horas_por_fecha,
    generar_grafico_horas_vs_promedio,
)
from persistencia import cargar_datos, guardar_datos
from reportes import mostrar_proyeccion_nota, mostrar_reporte
from utils import leer_entero


def requiere_estudiante_activo(sistema):
    """Verifica que haya un estudiante activo antes de entrar a un submenú.

    Puede quedar en None si se elimina el único estudiante (o el que
    estaba activo) desde la sección de Estudiantes.
    """
    if sistema.estudiante_activo is None:
        print(
            "No hay un estudiante activo. Vaya primero a 'Gestión "
            "académica' > sección Estudiantes, para registrar o elegir uno."
        )
        return False
    return True


def mostrar_menu_principal():

    print("\n===== SISTEMA DE RENDIMIENTO ACADÉMICO =====")
    print("1. Gestión académica")
    print("2. Reportes y análisis")
    print("3. Guardar archivo")
    print("4. Cargar archivo")
    print("0. Salir")
    return leer_entero("Seleccione una opción: ")


def iniciar_sesion(sistema):
    """"
    Garantiza que exista un estudiante activo antes de mostrar el
    menú principal. Si no hay estudiantes, obliga a registrar uno.
    Si hay exactamente uno, lo activa automáticamente. Si hay varios,
    pide elegir cuál usar.
    """
    if not sistema.estudiantes:
        print("No hay estudiantes registrados.")
        print("Debe registrar uno para poder usar el sistema.")
        registrar_estudiante(sistema)
        return

    if len(sistema.estudiantes) == 1:
        sistema.estudiante_activo = sistema.estudiantes[0]
        return

    print("Seleccione con qué estudiante desea trabajar:")
    cambiar_estudiante_activo(sistema)


def ejecutar_y_guardar(accion, sistema):
    
    accion(sistema)
    guardar_datos(sistema)


def menu_gestion_academica(sistema):
    
    while True:
        print("\n----- GESTIÓN ACADÉMICA -----")
        print("--- Estudiantes ---")
        print("1. Registrar estudiante")
        print("2. Actualizar estudiante")
        print("3. Cambiar estudiante activo")
        print("4. Eliminar estudiante")
        print("5. Ver estudiantes registrados")
        print("--- Cursos ---")
        print("6. Registrar curso(s)")
        print("7. Eliminar curso(s)")
        print("8. Consultar curso(s)")
        print("--- Evaluaciones ---")
        print("9. Registrar evaluación(es)")
        print("10. Actualizar evaluación")
        print("--- Horas de estudio ---")
        print("11. Registrar horas")
        print("12. Actualizar horas")
        print("0. Volver")
        opcion = leer_entero("Seleccione una opción: ")

        if opcion == 1:
            ejecutar_y_guardar(registrar_estudiante, sistema)
        elif opcion == 2:
            ejecutar_y_guardar(actualizar_estudiante, sistema)
        elif opcion == 3:
            ejecutar_y_guardar(cambiar_estudiante_activo, sistema)
        elif opcion == 4:
            ejecutar_y_guardar(eliminar_estudiante, sistema)
        elif opcion == 5:
            mostrar_estudiantes(sistema)
        elif opcion == 6:
            if requiere_estudiante_activo(sistema):
                ejecutar_y_guardar(registrar_curso, sistema)
        elif opcion == 7:
            if requiere_estudiante_activo(sistema):
                ejecutar_y_guardar(eliminar_cursos, sistema)
        elif opcion == 8:
            if requiere_estudiante_activo(sistema):
                consultar_cursos(sistema)
        elif opcion == 9:
            if requiere_estudiante_activo(sistema):
                ejecutar_y_guardar(registrar_evaluacion, sistema)
        elif opcion == 10:
            if requiere_estudiante_activo(sistema):
                ejecutar_y_guardar(actualizar_evaluacion, sistema)
        elif opcion == 11:
            if requiere_estudiante_activo(sistema):
                ejecutar_y_guardar(registrar_horas, sistema)
        elif opcion == 12:
            if requiere_estudiante_activo(sistema):
                ejecutar_y_guardar(actualizar_horas, sistema)
        elif opcion == 0:
            break
        else:
            print("Opción inválida.")


def menu_reportes(sistema):
    """Submenú de reportes y análisis."""
    while True:
        print("\n----- REPORTES Y ANÁLISIS -----")
        print("1. Ver reporte completo")
        print("2. Generar gráfico de barras")
        print("3. Ver proyección de nota necesaria")
        print("0. Volver")
        opcion = leer_entero("Seleccione una opción: ")

        if opcion == 1:
            mostrar_reporte(sistema)
        elif opcion == 2:
            generar_grafico_horas_vs_promedio(sistema.estudiante_activo)
            generar_grafico_evolucion(sistema.estudiante_activo)
            generar_grafico_horas_por_fecha(sistema.estudiante_activo)
        elif opcion == 3:
            mostrar_proyeccion_nota(sistema)
        elif opcion == 0:
            break
        else:
            print("Opción inválida.")


def main():
    """Punto de entrada del programa."""
    sistema = cargar_datos()

    iniciar_sesion(sistema)
    guardar_datos(sistema)

    while True:
        opcion = mostrar_menu_principal()

        if opcion == 1:
            menu_gestion_academica(sistema)
        elif opcion == 2:
            if requiere_estudiante_activo(sistema):
                menu_reportes(sistema)
        elif opcion == 3:
            guardar_datos(sistema)
            print(
                "Datos guardados correctamente. El historial se "
                "actualizó con el estado de hoy."
            )
        elif opcion == 4:
            sistema = cargar_datos()
            print("Datos cargados correctamente desde el archivo.")
        elif opcion == 0:
            print("Programa finalizado. Información guardada correctamente.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()

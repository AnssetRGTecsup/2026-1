import os

from gestion.registro import registrar_estudiante, registrar_curso
from gestion.actualizacion import actualizar_datos_estudiante, actualizar_evaluaciones, actualizar_horas_estudio
from gestion.eliminacion import eliminar_cursos
from reportes.impresion import imprimir_cursos
from reportes.graficos import grafico_barras, grafico_dispersion, grafico_creditos, grafico_evolucion_notas
from persistencia.guardar import guardar_datos
from persistencia.cargar import cargar_datos
from utilidades.menu import mostrar_menu


def submenu_graficos(estudiante):
    print("\n--- Generar Reporte Grafico ---")
    print("1. Grafico de Barras (promedios vs nota minima)")
    print("2. Grafico de Dispersion (horas vs nota final)")
    print("3. Grafico de Lineas (creditos por curso)")
    print("4. Grafico de Evolucion de Notas (por curso)")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        grafico_barras(estudiante)
    elif opcion == "2":
        grafico_dispersion(estudiante)
    elif opcion == "3":
        grafico_creditos(estudiante)
    elif opcion == "4":
        grafico_evolucion_notas(estudiante)
    else:
        print("Opcion invalida.\n")


def main():
    if not os.path.exists("datos"):
        os.makedirs("datos")

    estudiante = None
    activo = True

    while activo:
        mostrar_menu()
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            estudiante = registrar_estudiante()
        elif opcion == "2":
            actualizar_datos_estudiante(estudiante)
        elif opcion == "3":
            registrar_curso(estudiante)
        elif opcion == "4":
            actualizar_evaluaciones(estudiante)
        elif opcion == "5":
            actualizar_horas_estudio(estudiante)
        elif opcion == "6":
            eliminar_cursos(estudiante)
        elif opcion == "7":
            imprimir_cursos(estudiante)
        elif opcion == "8":
            guardar_datos(estudiante)
        elif opcion == "9":
            estudiante_cargado = cargar_datos()
            if estudiante_cargado is not None:
                estudiante = estudiante_cargado
        elif opcion == "10":
            submenu_graficos(estudiante)
        elif opcion == "11":
            print("\nSaliendo del sistema. ¡Hasta luego!\n")
            activo = False
        else:
            print("\nOpcion invalida, intente nuevamente.\n")


if __name__ == "__main__":
    main()

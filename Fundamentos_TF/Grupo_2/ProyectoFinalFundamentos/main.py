from RegistrarEstudiante import RegistrarEstudiante
from ActualizarEstudiante import ActualizarEstudiante
from RegistrarCurso import RegistrarCurso
from ActualizarEvaluaciones import ActualizarEvaluaciones
from ActualizarHoras import ActualizarHoras
from EliminarCurso import EliminarCurso
from ImprimirCursos import ImprimirCursos
from ArchivosSaves import GuardarArchivos, LeerArchivos
from ImprimirEstructura import ImprimirEstructuraDiccionario
from ReportesGraficos import EjecutarModuloGrafico
from GenerarDatosAleatorios import GenerarDatosAleatorios 
lista_estudiantes = []

def seleccionar_estudiante(estudiantes):
    if not estudiantes:
        print("\nNo hay estudiantes registrados en el sistema.")
        return None
    print("\n--- SELECCIONAR ESTUDIANTE ---")
    for i, est in enumerate(estudiantes, 1):
        print(f"{i}. {est['nombre']} ({est['codigo']})")
    
    while True:
        try:
            opc = int(input("Seleccione el número del estudiante: "))
            if 1 <= opc <= len(estudiantes):
                return estudiantes[opc - 1]
            print("Número fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

while True:
    print("\n=============================================")
    print("       SISTEMA DE RENDIMIENTO ACADÉMICO      ")
    print("=============================================")
    print(" 1. Registrar Estudiante")
    print(" 2. Actualizar Datos del Estudiante")
    print(" 3. Registrar Curso")
    print(" 4. Actualizar Evaluaciones")
    print(" 5. Actualizar Horas de Estudio")
    print(" 6. Eliminar Curso(s)")
    print(" 7. Imprimir Datos de Curso(s)")
    print(" 8. Guardar archivos")
    print(" 9. Leer archivos")
    print(" 10. Generar Datos Aleatorios de Prueba")
    print(" 11. Imprimir Registro Completo del estudiante")
    print(" 12. Generar Reportes Gráficos (Matplotlib y Seaborn)")
    print(" 13. Salir del programa")
    print("=============================================")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        RegistrarEstudiante(lista_estudiantes)
    elif opcion in ["2", "3", "4", "5", "6", "7", "11", "12"]:
        
        estudiante = seleccionar_estudiante(lista_estudiantes)
        if estudiante:
            if opcion == "2":
                ActualizarEstudiante(estudiante)
            elif opcion == "3":
                RegistrarCurso(estudiante)
            elif opcion == "4":
                ActualizarEvaluaciones(estudiante)
            elif opcion == "5":
                ActualizarHoras(estudiante)
            elif opcion == "6":
                EliminarCurso(estudiante)
            elif opcion == "7":
                ImprimirCursos(estudiante)
            elif opcion == "11":
                ImprimirEstructuraDiccionario(estudiante)
            elif opcion == "12":
                EjecutarModuloGrafico(estudiante)
    elif opcion == "8":
        GuardarArchivos(lista_estudiantes)
    elif opcion == "9":
        LeerArchivos(lista_estudiantes)
    elif opcion == "10":
        
        GenerarDatosAleatorios(lista_estudiantes)
    elif opcion == "13":
        print("\nGracias por usar el sistema. ¡Éxito en tus estudios!\n")
        break
    else:
        print("\nOpción no válida. Por favor, seleccione un número del menú.")
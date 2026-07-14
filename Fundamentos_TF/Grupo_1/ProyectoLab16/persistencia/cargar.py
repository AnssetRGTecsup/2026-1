from datetime import datetime

from modelos.entidades import Estudiante, Curso, Evaluacion, HabitoEstudio

RUTA_ARCHIVO = "datos/estudiante.txt"


def cargar_datos():
    try:
        archivo = open(RUTA_ARCHIVO, "r")
    except FileNotFoundError:
        print("\nNo se encontró ningún archivo guardado todavía. Use primero la opción 'Guardar Archivos'.\n")
        return None

    estudiante = None

    with archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if linea == "":
                continue

            partes = linea.split("|")
            tipo = partes[0]

            try:
                if tipo == "ESTUDIANTE":
                    estudiante = Estudiante(partes[1], partes[2], int(partes[3]))

                elif tipo == "CURSO" and estudiante is not None:
                    estudiante.agregar_curso(Curso(partes[1], int(partes[2])))

                elif tipo == "EVAL" and estudiante is not None:
                    curso = estudiante.buscar_curso(partes[1])
                    if curso is not None:
                        fecha = datetime.strptime(partes[5], "%d/%m/%Y").date()
                        curso.agregar_evaluacion(Evaluacion(partes[2], fecha, float(partes[3]), float(partes[4])))

                elif tipo == "HORAS" and estudiante is not None:
                    curso = estudiante.buscar_curso(partes[1])
                    if curso is not None:
                        fecha = datetime.strptime(partes[3], "%d/%m/%Y").date()
                        curso.agregar_habito_estudio(HabitoEstudio(fecha, float(partes[2])))

            except (ValueError, IndexError):
                print(f"Aviso: se ignoró la línea {numero_linea} del archivo por tener un formato inválido.")

    print("Archivo leído correctamente.")
    return estudiante

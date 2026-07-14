import os

RUTA_ARCHIVO = "datos/estudiante.txt"


def guardar_datos(estudiante):
    if estudiante is None:
        print("\nNo hay datos de estudiante para guardar.\n")
        return

    try:
        os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
        archivo = open(RUTA_ARCHIVO, "w")
    except OSError as error:
        print(f"\nNo se pudo guardar el archivo: {error}\n")
        return

    with archivo:
        linea = "ESTUDIANTE|" + estudiante.nombre + "|" + estudiante.codigo + "|" + str(estudiante.ciclo) + "\n"
        archivo.write(linea)

        for curso in estudiante.cursos:
            linea = "CURSO|" + curso.nombre + "|" + str(curso.creditos) + "\n"
            archivo.write(linea)

            for evaluacion in curso.evaluaciones:
                linea = ("EVAL|" + curso.nombre + "|" + evaluacion.nombre + "|" + str(evaluacion.nota) + "|"
                         + str(evaluacion.peso) + "|" + evaluacion.fecha_texto() + "\n")
                archivo.write(linea)

            for habito in curso.habitos_estudio:
                linea = "HORAS|" + curso.nombre + "|" + str(habito.horas) + "|" + habito.fecha_texto() + "\n"
                archivo.write(linea)

    print("Datos guardados correctamente en '" + RUTA_ARCHIVO + "'.\n")

def _imprimir_un_curso(curso):
    print("Curso:", curso.nombre)
    print("Créditos:", curso.creditos)

    print("Evaluaciones:")
    if len(curso.evaluaciones) == 0:
        print("  (sin evaluaciones registradas)")
    else:
        for evaluacion in curso.evaluaciones:
            print("  -", evaluacion)

    print("Horas de estudio registradas:")
    if len(curso.habitos_estudio) == 0:
        print("  (sin horas registradas)")
    else:
        for habito in curso.habitos_estudio:
            print("  -", habito)

   
    nota_final, horas_totales, aprobado = curso.resumen()
    estado = "Aprobado" if aprobado else "Desaprobado"
    print("Total de horas invertidas:", horas_totales)
    print("Nota final del curso:", nota_final, "->", estado)
    print()


def imprimir_cursos(estudiante):
    if estudiante is None or not estudiante.tiene_cursos():
        print("\nNo hay cursos registrados.\n")
        return

    print("\nImprimir Datos de Curso(s)")
    print("1. Imprimir un curso")
    print("2. Imprimir varios cursos")
    print("3. Imprimir todos los cursos")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre = input("Nombre del curso: ")
        curso = estudiante.buscar_curso(nombre)
        if curso is not None:
            _imprimir_un_curso(curso)
        else:
            print("Curso no encontrado.\n")

    elif opcion == "2":
        nombres = input("Nombres de los cursos separados por coma: ")
        for nombre in nombres.split(","):
            nombre = nombre.strip()
            curso = estudiante.buscar_curso(nombre)
            if curso is not None:
                _imprimir_un_curso(curso)
            else:
                print("Curso '" + nombre + "' no encontrado.")

    elif opcion == "3":
        for curso in estudiante.cursos:
            _imprimir_un_curso(curso)
        _imprimir_resumen_general(estudiante)

    else:
        print("Opción inválida.\n")


def _imprimir_resumen_general(estudiante):
    """Arma un diccionario {nombre_curso: nota_final} y muestra un resumen general."""
    resumen_por_curso = {}
    for curso in estudiante.cursos:
        resumen_por_curso[curso.nombre] = curso.calcular_nota_final()

    aprobados = 0
    for nota in resumen_por_curso.values():
        if nota >= 12:
            aprobados += 1

    print("--- Resumen general del ciclo ---")
    for nombre_curso, nota in resumen_por_curso.items():
        print(f"  {nombre_curso}: {nota}")
    print(f"Cursos aprobados: {aprobados} de {len(resumen_por_curso)}\n")

import matplotlib.pyplot as plt
import seaborn as sns

from modelos.entidades import Curso


def grafico_barras(estudiante):
    if estudiante is None or not estudiante.tiene_cursos():
        print("\nNo hay cursos registrados para graficar.\n")
        return

    nombres_cursos = []
    promedios = []

    for curso in estudiante.cursos:
        nombres_cursos.append(curso.nombre)
        promedios.append(curso.calcular_nota_final())

    plt.figure(figsize=(8, 5))
    plt.bar(nombres_cursos, promedios, color="skyblue")
    plt.axhline(y=Curso.NOTA_MINIMA_APROBATORIA, color="red", linestyle="-", label="Nota mínima aprobatoria (12)")
    plt.title("Promedio actual por curso")
    plt.xlabel("Curso")
    plt.ylabel("Promedio")
    plt.legend()
    plt.tight_layout()
    plt.show()


def grafico_dispersion(estudiante):
    if estudiante is None or not estudiante.tiene_cursos():
        print("\nNo hay cursos registrados para graficar.\n")
        return

    horas_totales = []
    notas_finales = []

    for curso in estudiante.cursos:
        horas_totales.append(curso.calcular_horas_totales())
        notas_finales.append(curso.calcular_nota_final())

    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=horas_totales, y=notas_finales, s=100, color="green")
    plt.title("Horas de estudio invertidas vs Nota final")
    plt.xlabel("Total de horas invertidas en el ciclo")
    plt.ylabel("Nota final obtenida")
    plt.tight_layout()
    plt.show()


def grafico_creditos(estudiante):
    if estudiante is None or not estudiante.tiene_cursos():
        print("\nNo hay cursos registrados para graficar.\n")
        return

    nombres_cursos = []
    creditos_cursos = []

    for curso in estudiante.cursos:
        nombres_cursos.append(curso.nombre)
        creditos_cursos.append(curso.creditos)

    plt.figure(figsize=(8, 5))
    plt.plot(nombres_cursos, creditos_cursos, color="purple", marker="o", linestyle="--")
    plt.title("Créditos por Curso")
    plt.xlabel("Curso")
    plt.ylabel("Créditos")
    plt.tight_layout()
    plt.show()


def grafico_evolucion_notas(estudiante):
    """Mejora adicional: muestra cómo evolucionó la nota de un curso, evaluación por evaluación."""
    if estudiante is None or not estudiante.tiene_cursos():
        print("\nNo hay cursos registrados para graficar.\n")
        return

    nombre_curso = input("Nombre del curso a graficar: ")
    curso = estudiante.buscar_curso(nombre_curso)

    if curso is None:
        print("Curso no encontrado.\n")
        return

    if len(curso.evaluaciones) == 0:
        print("Ese curso no tiene evaluaciones registradas.\n")
        return

    evaluaciones_ordenadas = sorted(curso.evaluaciones, key=lambda evaluacion: evaluacion.fecha)

    fechas = [evaluacion.fecha for evaluacion in evaluaciones_ordenadas]
    notas = [evaluacion.nota for evaluacion in evaluaciones_ordenadas]
    nombres_eval = [evaluacion.nombre for evaluacion in evaluaciones_ordenadas]

    plt.figure(figsize=(8, 5))
    plt.plot(fechas, notas, color="darkorange", marker="o", linestyle="-", linewidth=2)

    for x, y, nombre in zip(fechas, notas, nombres_eval):
        plt.annotate(nombre, (x, y), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9)

    plt.axhline(y=Curso.NOTA_MINIMA_APROBATORIA, color="red", linestyle="--", label="Nota mínima aprobatoria (12)")
    plt.title(f"Evolución de notas - {curso.nombre}")
    plt.xlabel("Fecha de evaluación")
    plt.ylabel("Nota")
    plt.ylim(0, 20)
    plt.xticks(rotation=30)
    plt.legend()
    plt.tight_layout()
    plt.show()

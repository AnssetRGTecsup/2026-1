from collections import defaultdict

import matplotlib.pyplot as plt

from utils import formatear_fecha_visual



def _grafico_barras_con_linea(categorias, valores_barra, valores_linea, titulo, xlabel,
    label_barra, label_linea, rotar_x=False):

    fig, eje_barra = plt.subplots(figsize=(8, 5))

    barras = eje_barra.bar(categorias, valores_barra, color="steelblue", label=label_barra)
    eje_barra.set_xlabel(xlabel)
    eje_barra.set_ylabel(label_barra, color="steelblue")
    eje_barra.tick_params(axis="y", labelcolor="steelblue")
    if rotar_x:
        eje_barra.tick_params(axis="x", rotation=45)

    eje_linea = eje_barra.twinx()
    linea = eje_linea.plot(
        categorias, valores_linea, color="darkorange", marker="o", label=label_linea
    )
    referencia = eje_linea.axhline(
        y=12, color="red", linestyle="--", label="Nota mínima aprobatoria"
    )
    eje_linea.set_ylabel(label_linea, color="darkorange")
    eje_linea.tick_params(axis="y", labelcolor="darkorange")
    eje_linea.set_ylim(0, 20)

    plt.title(titulo)

    handles = [barras, linea[0], referencia]
    labels = [h.get_label() for h in handles]
    eje_barra.legend(handles, labels, loc="upper left")

    fig.tight_layout()
    plt.show()


def generar_grafico_horas_vs_promedio(estudiante):

    cursos = [c for c in estudiante.cursos if c.evaluaciones]

    if not cursos:
        print("No existen evaluaciones para generar el gráfico.")
        return

    nombres = [curso.nombre for curso in cursos]
    horas = [curso.total_horas() for curso in cursos]
    promedios = [curso.promedio() for curso in cursos]

    _grafico_barras_con_linea(
        categorias=nombres,
        valores_barra=horas,
        valores_linea=promedios,
        titulo="Horas de estudio vs. Promedio por curso",
        xlabel="Cursos",
        label_barra="Horas de estudio",
        label_linea="Promedio",
    )


def generar_grafico_evolucion(estudiante):
    
    historial = estudiante.historial

    if len(historial) < 2:
        print(
            "Se necesitan al menos 2 sesiones guardadas (es decir, "
            "guardar el sistema en al menos 2 días distintos) para "
            "mostrar el progreso en el tiempo."
        )
        return

    fechas = [formatear_fecha_visual(entrada["fecha"]) for entrada in historial]
    promedios = [entrada["promedio_general"] for entrada in historial]
    horas = [entrada["horas_totales"] for entrada in historial]

    _grafico_barras_con_linea(
        categorias=fechas,
        valores_barra=horas,
        valores_linea=promedios,
        titulo="Progreso entre sesiones guardadas",
        xlabel="Sesión guardada (fecha)",
        label_barra="Horas totales acumuladas",
        label_linea="Promedio general",
        rotar_x=True,
    )


def generar_grafico_horas_por_fecha(estudiante):
    
    horas_por_fecha = defaultdict(float)

    for curso in estudiante.cursos:
        for registro in curso.horas_estudio:
            if registro["fecha"] is not None:
                horas_por_fecha[registro["fecha"]] += registro["horas"]

    if not horas_por_fecha:
        print(
            "No hay registros de horas con fecha conocida para generar "
            "este gráfico."
        )
        return

    fechas_ordenadas = sorted(horas_por_fecha.keys())
    fechas_visual = [formatear_fecha_visual(fecha) for fecha in fechas_ordenadas]
    horas = [round(horas_por_fecha[fecha], 2) for fecha in fechas_ordenadas]

    fig, eje = plt.subplots(figsize=(8, 5))
    eje.bar(fechas_visual, horas, color="seagreen")
    eje.set_xlabel("Fecha")
    eje.set_ylabel("Horas de estudio")
    eje.set_title("Horas de estudio reales por día (todos los cursos)")
    eje.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    plt.show()

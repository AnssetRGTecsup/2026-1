from analisis import (
    generar_conclusion,
    obtener_curso_mas_horas,
    obtener_curso_menos_horas,
    obtener_cursos_en_riesgo,
    obtener_mejor_curso,
    obtener_peor_curso,
)
from graficos import (
    generar_grafico_evolucion,
    generar_grafico_horas_por_fecha,
    generar_grafico_horas_vs_promedio,
)
from historial import mostrar_comparacion_ultima_sesion, mostrar_dias_estudiados
from utils import confirmar, leer_nota, seleccionar_curso_con_contexto


def mostrar_cursos_en_riesgo(en_riesgo):
   
    print("\n---------- Cursos en riesgo ----------")

    for curso in en_riesgo:
        peso_pendiente = round(1 - curso.peso_registrado(), 2)

        if peso_pendiente <= 0:
            print(
                f"{curso.nombre}: promedio final {curso.promedio():.2f}. "
                f"No queda peso pendiente para mejorar la nota."
            )
            continue

        necesaria = curso.nota_necesaria(12)

        if necesaria > 20:
            print(
                f"{curso.nombre}: promedio actual {curso.promedio():.2f}. "
                f"No es posible llegar a 12 aunque obtenga la nota máxima "
                f"en el {peso_pendiente * 100:.0f}% pendiente."
            )
        else:
            print(
                f"{curso.nombre}: promedio actual {curso.promedio():.2f}. "
                f"Necesita {necesaria:.2f} en el {peso_pendiente * 100:.0f}% "
                f"pendiente para aprobar."
            )


def mostrar_evolucion_por_curso(estudiante):
    
    cursos_comparables = [c for c in estudiante.cursos if len(c.evaluaciones) >= 2]

    if not cursos_comparables:
        return

    print("\n---------- Evolución por curso ----------")

    for curso in cursos_comparables:
        diferencia = curso.evolucion()

        if diferencia > 0:
            tendencia = f"mejoró (+{diferencia:.2f} puntos)"
        elif diferencia < 0:
            tendencia = f"empeoró ({diferencia:.2f} puntos)"
        else:
            tendencia = "se mantuvo igual"

        print(
            f"{curso.nombre}: {tendencia}. "
            f"Horas de estudio acumuladas: {curso.total_horas():.2f}."
        )


def mostrar_proyeccion_nota(sistema):
   
    estudiante = sistema.estudiante_activo

    curso = seleccionar_curso_con_contexto(estudiante)
    if curso is None:
        return

    meta = 12
    if confirmar("¿Desea usar una meta distinta a 12 (nota mínima aprobatoria)?"):
        meta = leer_nota("Meta a alcanzar (0-20): ")

    peso_pendiente = round(1 - curso.peso_registrado(), 2)

    if peso_pendiente <= 0:
        print(
            f"\nEl curso {curso.nombre} ya tiene el 100% del peso "
            f"registrado. No queda peso pendiente sobre el cual proyectar."
        )
        print(f"Promedio final: {curso.promedio():.2f}")
        return

    necesaria = curso.nota_necesaria(meta)

    print(f"\n--- Proyección para {curso.nombre} ---")
    print(f"Promedio acumulado hasta ahora: {curso.promedio():.2f}")
    print(f"Peso pendiente por evaluar: {peso_pendiente * 100:.0f}%")

    if necesaria <= 0:
        print(f"Ya alcanzó la meta de {meta} con lo registrado hasta ahora.")
    elif necesaria > 20:
        print(
            f"No es posible alcanzar la meta de {meta} con el peso "
            f"pendiente: necesitaría una nota de {necesaria:.2f}, "
            f"superior al máximo de 20."
        )
    else:
        print(
            f"Necesita una nota de {necesaria:.2f} en el peso "
            f"restante para llegar a {meta}."
        )


def mostrar_reporte(sistema):
    """Muestra el reporte del estudiante activo."""

    estudiante = sistema.estudiante_activo

    if estudiante is None:
        print("Debe seleccionar un estudiante primero.")
        return

    promedio = estudiante.promedio_general()
    mejor = obtener_mejor_curso(estudiante)
    peor = obtener_peor_curso(estudiante)
    mas_horas = obtener_curso_mas_horas(estudiante)
    menos_horas = obtener_curso_menos_horas(estudiante)

    print("\n========== REPORTE ACADÉMICO ==========")

    print(f"Nombre : {estudiante.nombre}")
    print(f"Código : {estudiante.codigo}")
    print(f"Ciclo  : {estudiante.ciclo}")

    print("\n---------- Resumen ----------")

    print(f"Promedio general: {promedio:.2f}")

    if mejor:
        print(
            f"Mejor curso: {mejor.nombre} "
            f"({mejor.promedio():.2f})"
        )

    if peor:
        print(
            f"Curso con menor rendimiento: {peor.nombre} "
            f"({peor.promedio():.2f})"
        )

    if mas_horas:
        print(
            f"Curso donde más estudió: {mas_horas.nombre} "
            f"({mas_horas.total_horas()} horas)"
        )

    if menos_horas:
        print(
            f"Curso donde menos estudió: {menos_horas.nombre} "
            f"({menos_horas.total_horas()} horas)"
        )

    print("\n---------- Diagnóstico ----------")

    print(
        generar_conclusion(
            promedio,
            mejor,
            peor,
            mas_horas,
            menos_horas
        )
    )

    en_riesgo = obtener_cursos_en_riesgo(estudiante)
    if en_riesgo:
        mostrar_cursos_en_riesgo(en_riesgo)

    mostrar_evolucion_por_curso(estudiante)

    mostrar_comparacion_ultima_sesion(estudiante)

    mostrar_dias_estudiados(estudiante)

    if confirmar("\n¿Desea generar los gráficos?"):
        generar_grafico_horas_vs_promedio(estudiante)
        generar_grafico_evolucion(estudiante)
        generar_grafico_horas_por_fecha(estudiante)

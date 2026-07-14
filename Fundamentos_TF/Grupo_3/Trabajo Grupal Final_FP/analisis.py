""" Cálculo y análisis puro sobre los datos del estudiante"""
from datetime import date, timedelta


def obtener_mejor_curso(estudiante):
    
    mejor = None
    for curso in estudiante.cursos:
        if curso.evaluaciones:
            if mejor is None or curso.promedio() > mejor.promedio():
                mejor = curso
    return mejor


def obtener_peor_curso(estudiante):
    
    peor = None
    for curso in estudiante.cursos:
        if curso.evaluaciones:
            if peor is None or curso.promedio() < peor.promedio():
                peor = curso
    return peor


def obtener_curso_mas_horas(estudiante):
    
    mas_horas = None
    for curso in estudiante.cursos:
        if mas_horas is None or curso.total_horas() > mas_horas.total_horas():
            mas_horas = curso
    return mas_horas


def obtener_curso_menos_horas(estudiante):
   
    menos_horas = None
    for curso in estudiante.cursos:
        if menos_horas is None or curso.total_horas() < menos_horas.total_horas():
            menos_horas = curso
    return menos_horas


def obtener_cursos_en_riesgo(estudiante):
    
    return [
        curso for curso in estudiante.cursos
        if curso.evaluaciones and curso.promedio() < 12
    ]


def calcular_dias_estudiados(estudiante, dias=7):
    """ Analiza los últimos dias del estudiante sus registros de hora de estudio """
    hoy = date.today()

    rango_fechas = []
    for i in range(dias):
        fecha_del_rango = (hoy - timedelta(days=i)).isoformat()
        rango_fechas.append(fecha_del_rango)

    fechas_con_estudio = set()
    for curso in estudiante.cursos:
        for registro in curso.horas_estudio:
            if registro["fecha"] is not None:
                fechas_con_estudio.add(registro["fecha"])

    dias_estudiados = 0
    fechas_sin_estudio = []
    for fecha in rango_fechas:
        if fecha in fechas_con_estudio:
            dias_estudiados = dias_estudiados + 1
        else:
            fechas_sin_estudio.append(fecha)

    return dias_estudiados, dias, fechas_sin_estudio


def generar_conclusion(promedio, mejor, peor, mas_horas, menos_horas):
    """Genera un diagnóstico académico en texto"""

    diagnostico = []

    if promedio >= 17:
        diagnostico.append(
            "El estudiante presenta un rendimiento académico excelente."
        )
    elif promedio >= 14:
        diagnostico.append(
            "El estudiante presenta un buen rendimiento académico."
        )
    elif promedio >= 11:
        diagnostico.append(
            "El estudiante presenta un rendimiento aceptable, pero aún puede mejorar."
        )
    else:
        diagnostico.append(
            "El estudiante presenta un rendimiento bajo y requiere reforzar sus hábitos de estudio."
        )

    if mejor:
        diagnostico.append(
            f"Su mejor desempeño corresponde al curso de {mejor.nombre}."
        )

    if peor:
        diagnostico.append(
            f"El curso que requiere mayor atención es {peor.nombre}."
        )

    hay_cursos_distintos = mejor and peor and mejor.nombre != peor.nombre

    coincidencias = [
        (mejor, mas_horas,
         "Se observa que el curso donde más estudia también es su mejor "
         "curso, lo que sugiere que el tiempo de estudio está "
         "contribuyendo positivamente a su rendimiento."),
        (peor, menos_horas,
         "El curso donde menos estudia coincide con su menor rendimiento, "
         "por lo que sería recomendable dedicarle más tiempo."),
        (peor, mas_horas,
         "Aunque dedica muchas horas a este curso, el rendimiento "
         "continúa siendo bajo. Esto puede indicar que debe revisar su "
         "forma de estudio."),
        (mejor, menos_horas,
         "Obtiene un buen rendimiento en este curso con pocas horas de "
         "estudio, lo que demuestra un buen dominio de los contenidos."),
    ]

    for curso_rendimiento, curso_horas, mensaje in coincidencias:
        if (
            hay_cursos_distintos
            and curso_horas
            and curso_rendimiento.nombre == curso_horas.nombre
        ):
            diagnostico.append(mensaje)

    return " ".join(diagnostico)

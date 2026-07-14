from analisis import calcular_dias_estudiados
from utils import formatear_fecha_visual

def mostrar_comparacion_ultima_sesion(estudiante):
    """ Solo es posible gracias al historial que se guarda en el JSON entre
    sesiones; sin persistencia, esta comparación no podría existir."""
    historial = estudiante.historial

    print("\n---------- Comparación con tu última sesión guardada ----------")

    if len(historial) < 2:
        print(
            "Aún no hay suficiente historial para comparar. Se necesitan "
            "al menos 2 sesiones guardadas en días distintos."
        )
        return

    anterior = historial[-2]
    actual = historial[-1]

    fecha_anterior = formatear_fecha_visual(anterior["fecha"])
    fecha_actual = formatear_fecha_visual(actual["fecha"])

    diferencia_promedio = round(
        actual["promedio_general"] - anterior["promedio_general"], 2
    )
    diferencia_horas = round(
        actual["horas_totales"] - anterior["horas_totales"], 2
    )

    if diferencia_promedio > 0:
        tendencia_promedio = (
            f"subió de {anterior['promedio_general']:.2f} a "
            f"{actual['promedio_general']:.2f} (+{diferencia_promedio:.2f})"
        )
    elif diferencia_promedio < 0:
        tendencia_promedio = (
            f"bajó de {anterior['promedio_general']:.2f} a "
            f"{actual['promedio_general']:.2f} ({diferencia_promedio:.2f})"
        )
    else:
        tendencia_promedio = f"se mantuvo en {actual['promedio_general']:.2f}"

    print(f"Desde el {fecha_anterior} hasta el {fecha_actual}: tu promedio {tendencia_promedio}.")

    if diferencia_horas > 0:
        print(f"Estudiaste {diferencia_horas:.2f} horas adicionales en ese período.")
    elif diferencia_horas < 0:
        print(
            f"Registraste {abs(diferencia_horas):.2f} horas menos que en "
            f"la sesión anterior."
        )
    else:
        print("No se registraron horas adicionales de estudio en ese período.")

    peor_anterior = anterior.get("peor_curso")
    peor_actual = actual.get("peor_curso")
    if peor_anterior and peor_actual:
        if peor_anterior == peor_actual:
            print(f"Tu curso más débil sigue siendo {peor_actual}.")
        else:
            print(f"Tu curso más débil cambió de {peor_anterior} a {peor_actual}.")

    mejor_anterior = anterior.get("mejor_curso")
    mejor_actual = actual.get("mejor_curso")
    if mejor_anterior and mejor_actual:
        if mejor_anterior == mejor_actual:
            print(f"Tu mejor curso sigue siendo {mejor_actual}.")
        else:
            print(f"Tu mejor curso cambió de {mejor_anterior} a {mejor_actual}.")


def mostrar_dias_estudiados(estudiante, dias=7):
    """acá solo se decide cómo presentarlo en consola."""
    dias_estudiados, dias_totales, fechas_sin_estudio = calcular_dias_estudiados(
        estudiante, dias
    )

    print(f"\n---------- Hábito de estudio (últimos {dias_totales} días) ----------")
    print(f"Estudiaste {dias_estudiados} de los últimos {dias_totales} días.")

    if not fechas_sin_estudio:
        print("¡Estudiaste todos los días del período! Excelente constancia.")
        return

    fechas_visual = ", ".join(
        formatear_fecha_visual(fecha) for fecha in fechas_sin_estudio
    )
    print(f"Días sin ningún registro de estudio: {fechas_visual}.")

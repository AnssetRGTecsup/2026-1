from utils import (
    formatear_fecha_visual,
    leer_horas,
    mostrar_contexto,
    seleccionar_curso_con_contexto,
    seleccionar_indice,
)



def registrar_horas(sistema):
    
    estudiante = sistema.estudiante_activo
    mostrar_contexto(estudiante)

    if not estudiante.cursos:
        print("Debe registrar al menos un curso antes de registrar horas.")
        return

    print(f"Tiene {len(estudiante.cursos)} curso(s). Ingrese las horas de cada uno:\n")

    for curso in estudiante.cursos:
        horas = leer_horas(f"{curso.nombre}: ")
        curso.agregar_horas(horas)

    print("\nHoras registradas correctamente en todos los cursos.")


def actualizar_horas(sistema):
    
    estudiante = sistema.estudiante_activo

    curso = seleccionar_curso_con_contexto(estudiante)
    if curso is None:
        return

    if not curso.horas_estudio:
        print("Este curso no tiene registros de horas.")
        return

    indice = seleccionar_indice(
        curso.horas_estudio, "el registro", _formatear_registro_horas
    )
    if indice is None:
        return

    nuevas_horas = leer_horas("Nuevas horas: ")
    curso.actualizar_horas(indice, nuevas_horas)
    print("Registro actualizado correctamente. La fecha del registro no cambia.")


def _formatear_registro_horas(registro):

    if registro["fecha"] is None:
        fecha_texto = "fecha desconocida"
    else:
        fecha_texto = formatear_fecha_visual(registro["fecha"])
    return f"{fecha_texto}: {registro['horas']} horas"

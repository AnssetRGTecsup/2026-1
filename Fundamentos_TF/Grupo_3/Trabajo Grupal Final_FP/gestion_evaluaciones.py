from utils import (
    confirmar,
    leer_entero,
    leer_fecha,
    leer_nota,
    leer_peso,
    leer_texto,
    mostrar_contexto,
    seleccionar_curso_con_contexto,
    seleccionar_indice,
)



def registrar_evaluacion(sistema):
    """ Recorre automáticamente cada curso registrado del estudiante activo """
    estudiante = sistema.estudiante_activo
    mostrar_contexto(estudiante)

    if not estudiante.cursos:
        print("Debe registrar al menos un curso antes de registrar evaluaciones.")
        return

    print(f"Tiene {len(estudiante.cursos)} curso(s) registrado(s).\n")

    for curso in estudiante.cursos:
        disponible = round(1 - curso.peso_registrado(), 2)

        if disponible <= 0:
            print(f"{curso.nombre}: ya tiene el 100% del peso registrado. Se omite.\n")
            continue

        if not confirmar(f"¿Desea registrar evaluaciones en {curso.nombre}?"):
            continue

        mostrar_contexto(estudiante, curso)
        cantidad = leer_entero(f"¿Cuántas evaluaciones va a registrar en {curso.nombre}?: ")

        for numero in range(1, cantidad + 1):
            disponible = round(1 - curso.peso_registrado(), 2)
            if disponible <= 0:
                print(
                    f"Ya no queda peso disponible en {curso.nombre}. "
                    f"Se detiene el registro para este curso."
                )
                break

            print(f"\n--- Evaluación {numero} de {cantidad} ({curso.nombre}) ---")
            nombre = leer_texto("Nombre de la evaluación: ")
            fecha = leer_fecha("Fecha")
            nota = leer_nota("Nota (0-20): ")

            print(f"Peso disponible en {curso.nombre}: {disponible * 100:.0f}%")
            peso = leer_peso("Peso en porcentaje: ")

            if peso > disponible + 1e-9:
                print(
                    f"Error: el peso excede el {disponible * 100:.0f}% "
                    f"disponible. Evaluación no registrada."
                )
                continue

            curso.agregar_evaluacion(nombre, fecha, nota, peso)

        print()

    print("Proceso de registro de evaluaciones finalizado.")


def actualizar_evaluacion(sistema):
    """Actualiza la nota y el peso de una evaluación existente."""
    estudiante = sistema.estudiante_activo

    curso = seleccionar_curso_con_contexto(estudiante)
    if curso is None:
        return

    if not curso.evaluaciones:
        print("Este curso no tiene evaluaciones registradas.")
        return

    nombres = list(curso.evaluaciones.keys())

    def formatear_evaluacion(nombre):
        ev = curso.evaluaciones[nombre]
        return f"{nombre} | Nota: {ev['nota']} | Peso: {ev['peso'] * 100:.0f}%"

    indice = seleccionar_indice(nombres, "la evaluación", formatear_evaluacion)
    if indice is None:
        return

    nombre_evaluacion = nombres[indice]
    peso_actual = curso.evaluaciones[nombre_evaluacion]["peso"]
    disponible = round(1 - curso.peso_registrado() + peso_actual, 2)

    nueva_nota = leer_nota("Nueva nota (0-20): ")
    print(f"Peso disponible (incluyendo el actual): {disponible * 100:.0f}%")
    nuevo_peso = leer_peso("Nuevo peso en porcentaje: ")

    if nuevo_peso > disponible + 1e-9:
        print("Error: el peso excede el disponible. No se actualizó.")
        return

    curso.actualizar_evaluacion(nombre_evaluacion, nueva_nota, nuevo_peso)
    print("Evaluación actualizada correctamente.")
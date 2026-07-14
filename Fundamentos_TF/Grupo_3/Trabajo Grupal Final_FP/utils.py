

from datetime import datetime

# ============================================================
# SECCIÓN 1: LECTURA — pedir y validar datos del usuario
# ============================================================


def leer_entero(mensaje):
   
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese un número entero.")


def leer_float(mensaje):
   
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingrese un número válido.")


def leer_texto(mensaje):
   
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: el texto no puede estar vacío.")


def leer_nombre(mensaje):
   
    while True:
        nombre = input(mensaje).strip()
        if nombre and all(parte.isalpha() for parte in nombre.split()):
            return nombre
        print("Error: el nombre solo debe contener letras y espacios.")


def leer_nota(mensaje):
   
    while True:
        nota = leer_float(mensaje)
        if 0 <= nota <= 20:
            return nota
        print("Error: la nota debe estar entre 0 y 20.")


def leer_peso(mensaje):
   
    while True:
        porcentaje = leer_float(mensaje)
        if 0 < porcentaje <= 100:
            return round(porcentaje / 100, 4)
        print("Error: el porcentaje debe ser mayor que 0 y hasta 100.")


def leer_creditos(mensaje):
    
    while True:
        creditos = leer_entero(mensaje)
        if creditos > 0:
            return creditos
        print("Error: los créditos deben ser mayores que cero.")


def leer_horas(mensaje):
   
    while True:
        horas = leer_float(mensaje)
        if horas >= 0:
            return horas
        print("Error: las horas no pueden ser negativas.")


def leer_fecha(mensaje):
   
    while True:
        texto = input(f"{mensaje} (D/M/A): ").strip()
        try:
            fecha = datetime.strptime(texto, "%d/%m/%Y")
            return fecha.strftime("%Y-%m-%d")
        except ValueError:
            print("Error: use el formato D/M/A, por ejemplo 9/7/2026.")


def confirmar(mensaje):
   
    while True:
        respuesta = input(f"{mensaje} (S/N): ").strip().upper()
        if respuesta == "S":
            return True
        if respuesta == "N":
            return False
        print("Error: responda únicamente con S o N.")



# SECCIÓN 2 VISUALIZACIÓN — mostrar/formatear datos ya existentes



def formatear_fecha_visual(fecha_iso):
    
    fecha = datetime.strptime(fecha_iso, "%Y-%m-%d")
    return f"{fecha.day}/{fecha.month}/{fecha.year}"


def mostrar_contexto(estudiante, curso=None):
    
    print("=" * 50)
    print(
        f"Estudiante activo: {estudiante.nombre} | "
        f"Código: {estudiante.codigo} | Ciclo: {estudiante.ciclo}"
    )
    if curso:
        print(f"Curso seleccionado: {curso.nombre}")
    print("=" * 50)



# SECCIÓN 3 SELECCIÓN — elegir uno o varios elementos de una lista



def seleccionar_uno(lista, etiqueta="elemento"):
    
    if not lista:
        print(f"No hay {etiqueta}s registrados.")
        return None

    for numero, item in enumerate(lista, start=1):
        print(f"{numero}. {item.nombre}")
    print("0. Cancelar")

    indice = leer_entero("Seleccione una opción: ")

    if indice == 0:
        return None
    if 1 <= indice <= len(lista):
        return lista[indice - 1]

    print("Opción inválida.")
    return None


def seleccionar_varios(lista, etiqueta="elemento"):
   
    if not lista:
        print(f"No hay {etiqueta}s registrados.")
        return []

    for numero, item in enumerate(lista, start=1):
        print(f"{numero}. {item.nombre}")

    entrada = input(
       
    ).strip().lower()

    if entrada == "todos":
        return lista

    seleccionados = []
    for parte in entrada.split(","):
        parte = parte.strip()
        if parte.isdigit() and 1 <= int(parte) <= len(lista):
            seleccionados.append(lista[int(parte) - 1])

    if not seleccionados:
        print("No se seleccionó ningún elemento válido.")

    return seleccionados


def seleccionar_indice(items, etiqueta, formatear):
    
    if len(items) == 1:
        print(f"Solo hay un registro: {formatear(items[0])}. Se actualizará directamente.")
        return 0

    for numero, item in enumerate(items, start=1):
        print(f"{numero}. {formatear(item)}")

    indice = leer_entero(f"Seleccione {etiqueta} a actualizar: ") - 1

    if 0 <= indice < len(items):
        return indice

    print("Opción inválida.")
    return None


def seleccionar_curso_con_contexto(estudiante):
   
    mostrar_contexto(estudiante)

    curso = seleccionar_uno(estudiante.cursos, "curso")
    if curso is None:
        return None

    mostrar_contexto(estudiante, curso)
    return curso
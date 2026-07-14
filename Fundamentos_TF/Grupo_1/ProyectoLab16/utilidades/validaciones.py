
from datetime import datetime


def leer_entero(mensaje):
    texto = input(mensaje).strip()
    try:
        return (True, int(texto))
    except ValueError:
        return (False, None)


def leer_flotante(mensaje):
    texto = input(mensaje).strip().replace(",", ".")
    try:
        return (True, float(texto))
    except ValueError:
        return (False, None)


def leer_fecha(mensaje):
    texto = input(mensaje).strip()
    try:
        fecha = datetime.strptime(texto, "%d/%m/%Y").date()
        return (True, fecha)
    except ValueError:
        return (False, None)

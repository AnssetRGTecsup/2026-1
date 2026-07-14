from datetime import datetime

def ConvertirFecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        return None
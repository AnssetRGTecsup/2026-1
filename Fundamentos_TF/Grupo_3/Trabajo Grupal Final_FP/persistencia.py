import json

from sistema import SistemaAcademico, crear_sistema_desde_dict


def guardar_datos(sistema, archivo="datos.json"):

    if sistema.estudiante_activo is not None:
        sistema.estudiante_activo.registrar_avance_del_dia()

    with open(archivo, "w", encoding="utf-8") as archivo_json:
        json.dump(
            sistema.to_dict(),
            archivo_json,
            indent=4,
            ensure_ascii=False
        )


def cargar_datos(archivo="datos.json"):
    
    try:
        with open(archivo, "r", encoding="utf-8") as archivo_json:
            datos = json.load(archivo_json)

        return crear_sistema_desde_dict(datos)

    except (FileNotFoundError, json.JSONDecodeError):
        return SistemaAcademico()

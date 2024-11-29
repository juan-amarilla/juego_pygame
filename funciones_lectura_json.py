import json


def leer_objetos(nombre_archivo: str) -> dict:
    """
    Lee un archivo tipo json

    Args:
    nombre_archivo(str)

    Return:
    retornara el contenido
    """

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(ruta: str, datos: dict) -> None:
    """
    Guarda los datos en un archivo json

    Args:
    ruta(str)
    datos(dict)

    Return:
    None
    """
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

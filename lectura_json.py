import json

def leer_objetos(nombre_archivo: str) -> dict:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos


# Función para guardar datos en un archivo JSON
def guardar_datos(ruta, datos):
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
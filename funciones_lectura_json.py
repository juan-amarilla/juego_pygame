import json


def leer_objetos(nombre_archivo: str) -> dict:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos


# # Función para guardar datos en un archivo JSON
# def guardar_datos(ruta, datos):
#     with open(ruta, 'w') as archivo:
#         json.dump(datos, archivo, indent=4)


def guardar_datos(archivo, datos_nuevos):
    """
    Guarda los datos en un archivo JSON. Si el archivo no existe, lo crea.
    Si ya existe, agrega los datos nuevos a la lista.
    """
    try:
        # Intenta leer el archivo
        with open(archivo, "r") as file:
            datos = json.load(file)
        # Asegúrate de que los datos sean una lista
        if not isinstance(datos, list):
            datos = [datos]
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío, inicializa como lista
        datos = []

    # Agregar los nuevos datos a la lista
    datos.append(datos_nuevos)

    # Escribir los datos actualizados en el archivo
    with open(archivo, "w") as file:
        json.dump(datos, file, indent=4)

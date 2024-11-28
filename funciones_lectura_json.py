"""
Módulo de funciones para leer y guardar datos en archivos JSON.

Este módulo proporciona funciones para leer objetos de un archivo JSON y guardarlos en dicho archivo.
Además, permite añadir nuevos datos a un archivo JSON existente, manteniendo el historial de los mismos.

Funciones:
- leer_objetos(nombre_archivo): Lee los datos de un archivo JSON y los devuelve como un diccionario.
- guardar_datos(archivo, datos_nuevos): Guarda los nuevos datos en un archivo JSON, agregándolos a la lista existente.

Excepciones manejadas:
- FileNotFoundError: Si el archivo no existe, se crea uno nuevo.
- JSONDecodeError: Si el archivo no contiene datos válidos en formato JSON, se inicializa como una lista vacía.
"""
import json


def leer_objetos(nombre_archivo: str) -> dict:
    """
    Lee un archivo JSON y devuelve su contenido como un diccionario.

    Parámetros:
    nombre_archivo (str): El nombre del archivo JSON que se va a leer.

    Retorna:
    dict: Los datos leídos desde el archivo JSON, como un diccionario.

    Excepciones:
    - Si el archivo no se puede abrir o no es válido, se lanza una excepción de Python.
    """
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos


def guardar_datos(archivo, datos_nuevos):
    """
    Guarda nuevos datos en un archivo JSON. Si el archivo no existe, lo crea. 
    Si ya existe, agrega los datos nuevos a la lista de datos existentes.

    Parámetros:
    archivo (str): El nombre del archivo JSON donde se almacenarán los datos.
    datos_nuevos (dict): Los nuevos datos que se agregarán al archivo JSON.

    Excepciones:
    - Si el archivo no se puede abrir o es inválido, maneja los errores y crea un nuevo archivo.
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

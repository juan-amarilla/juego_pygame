import random
from lectura_json import leer_objetos
from clases import Objeto


def generar_bombas(objetos, bombas_max):
    """
    Genera nuevas bombas si el número de bombas activas es menor al máximo permitido.

    :param objetos: Lista de objetos en el juego.
    :param max_bombas: Máximo número de bombas activas.
    """
    bombas_activas = []
    for obj in objetos:
        if obj.tipo == "bomba":
            bombas_activas.append(obj)
    while len(bombas_activas) < bombas_max:
        direccion = random.choice(["vertical", "horizontal"])
        nueva_bomba = Objeto("bomba", direccion=direccion)
        objetos.append(nueva_bomba)
        bombas_activas.append(nueva_bomba)


def cargar_objetos(nombre_archivo):
    # Leer los datos del archivo JSON
    datos = leer_objetos(nombre_archivo)

    # Inicializar las listas
    objetos = []
    objetivos = []

    # Crear los objetos de acuerdo al archivo JSON
    for entrada in datos["objetos"]:
        tipo = entrada["tipo"]
        cantidad = entrada["cantidad"]
        for _ in range(cantidad):
            nuevo_objeto = Objeto(tipo)
            objetos.append(nuevo_objeto)
            if tipo == "tesoro" or tipo == "vida":
                # Agregar a la lista de objetivos
                objetivos.append(nuevo_objeto)

    # Crear bombas con diferentes direcciones
    for _ in range(cantidad):  # 10 bombas de caída
        objetos.append(Objeto("bomba", direccion="vertical"))

    for _ in range(cantidad):  # 5 bombas de movimiento lateral
        objetos.append(Objeto("bomba", direccion="horizontal"))

    # Devolver las listas de objetos y objetivos
    return objetos, objetivos

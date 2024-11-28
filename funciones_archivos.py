# pylint: disable=no-member
import pygame
from constantes_inicio import SONIDO_TECLADO_MENU
from funciones_pantalla import colocar_puntuaciones


def leer_archivo(ruta: str, ejecutar: bool, vertical: int, posicion: int) -> None:
    """
    Lee el archivo

    Args:
    ruta(str)
    ejecutar(bool)
    vertical(int)
    posicion(int)

    Returns:
    None
    """

    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    while ejecutar:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                ejecutar = False

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    SONIDO_TECLADO_MENU.play()
                    ejecutar = False

        colocar_puntuaciones(lineas, vertical, posicion)

    return ejecutar


def agregar_jugador(ruta: str, jugador: str) -> None:
    """
    Agrega un jugador con su puntuacion en el archivo ya elegido

    Args:
    ruta(str)
    jugador(str)

    Returns:
    None
    """

    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(jugador + "\n")

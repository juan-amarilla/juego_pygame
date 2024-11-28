# pylint: disable=no-member
"""
Este módulo define las constantes utilizadas en el juego.

Incluye configuraciones generales del juego, como el tamaño de la pantalla,
nombre del juego, límites de objetos en pantalla, así como la carga de
sonidos e imágenes para los elementos del juego.
"""

import pygame

pygame.init()

ANCHO = 800
ALTO = 600
NOMBRE_JUEGO = "Aventura en el Lugar de Escape"
BOMBAS_MAX = 2

# Cargar sonidos
SONIDO_TESORO = pygame.mixer.Sound("recursos_juego/sonidos/sonido_tesoro.mp3")
SONIDO_VIDA = pygame.mixer.Sound("recursos_juego/sonidos/sonido_vida.mp3")
SONIDO_BOMBA = pygame.mixer.Sound(
    "recursos_juego/sonidos/sonido_explosion.mp3")

# Cargar la imagen del fondo
FONDO = pygame.image.load("recursos_juego/imagenes/Bosque.png")
FONDO = pygame.transform.scale(FONDO, (ANCHO, ALTO))
FONDO_ANCHO = FONDO.get_width()
FONDO_1 = 0
FONDO_2 = FONDO_ANCHO
VELOCIDAD_FONDO = 2

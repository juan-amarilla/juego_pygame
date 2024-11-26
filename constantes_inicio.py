# pylint: disable=no-member
import pygame

pygame.init()
pygame.mixer.init()
ANCHO, ALTURA = 800, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTURA))
TITULO = "Aventura en el Lugar de Escape"
pygame.display.set_caption(TITULO)
TIPO_FUENTE = pygame.font.Font("recursos_menu/fuentes/pixel.ttf", 50)
SONIDO_TECLADO_MENU = pygame.mixer.Sound("recursos_menu/sonidos/sonido.ogg")
OPCIONES = ("Jugar", "Puntuaciones", "Salir")

POSICION = 100
VERTICAL = 255


COLORES = {
    "COLOR_TEXTO": (255, 200, 155),
    "COLOR_RECTANGULO": (0, 255, 0)
}

IMAGENES = {
    "PRIMER": pygame.transform.scale(pygame.image.load("recursos_menu/imagenes/imagen_menu/uno.png"), (800, 600)),
    "SEGUNDO": pygame.transform.scale(pygame.image.load("recursos_menu/imagenes/imagen_menu/dos.png"), (800, 600)),
    "TERCER": pygame.transform.scale(pygame.image.load("recursos_menu/imagenes/imagen_menu/tres.png"), (800, 600)),
    "CUARTO": pygame.transform.scale(pygame.image.load("recursos_menu/imagenes/imagen_menu/cuatro.png"), (800, 600))
}

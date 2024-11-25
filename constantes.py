import pygame

pygame.mixer.init()
PANTALLA = pygame.display.set_mode((800, 600))
POSICION = 100
VERTICAL = 255
SONIDO_TECLADO_MENU = pygame.mixer.Sound("sonidos/sonido.ogg")
OPCIONES = ("Jugar", "Puntuaciones", "Salir")


COLORES = {
    "COLOR_TEXTO": (255, 200, 155),
    "COLOR_RECTANGULO": (0, 255, 0)
}

IMAGENES = {
    "PRIMER": pygame.transform.scale(pygame.image.load("imagenes/imagen_menu/uno.png"), (800, 600)),
    "SEGUNDO": pygame.transform.scale(pygame.image.load("imagenes/imagen_menu/dos.png"), (800, 600)),
    "TERCER": pygame.transform.scale(pygame.image.load("imagenes/imagen_menu/tres.png"), (800, 600)),
    "CUARTO": pygame.transform.scale(pygame.image.load("imagenes/imagen_menu/cuatro.png"), (800, 600))
}
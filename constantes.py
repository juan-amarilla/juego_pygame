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

##############################

NOMBRE_JUEGO = "Aventura en el Lugar de Escape"
ANCHO = 800
ALTO = 600
BOMBAS_MAX = 2

# Cargar sonidos
SONIDO_TESORO = pygame.mixer.Sound("recursos/sonidos/sonido_tesoro.mp3")
SONIDO_VIDA = pygame.mixer.Sound("recursos/sonidos/sonido_vida.mp3")
SONIDO_BOMBA = pygame.mixer.Sound("recursos/sonidos/sonido_explosion.mp3")

# Cargar la imagen del fondo
FONDO = pygame.image.load("recursos/imagenes/Bosque.png")
FONDO = pygame.transform.scale(FONDO, (ANCHO, ALTO))
FONDO_ANCHO = FONDO.get_width()
FONDO_1 = 0
FONDO_2 = FONDO_ANCHO
VELOCIDAD_FONDO = 2
NOMBRE_JUEGO = "Aventura en el Lugar de Escape"
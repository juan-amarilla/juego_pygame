import pygame

ANCHO = 800
ALTO = 600
NOMBRE_JUEGO = "Aventura en el Lugar de Escape"
BOMBAS_MAX = 2

SONIDO_TESORO = pygame.mixer.Sound("recursos_juego/sonidos/sonido_tesoro.mp3")
SONIDO_VIDA = pygame.mixer.Sound("recursos_juego/sonidos/sonido_vida.mp3")
SONIDO_BOMBA = pygame.mixer.Sound(
    "recursos_juego/sonidos/sonido_explosion.mp3")

FONDO = pygame.image.load("recursos_juego/imagenes/Bosque.png")
FONDO = pygame.transform.scale(FONDO, (ANCHO, ALTO))
FONDO_ANCHO = FONDO.get_width()
FONDO_1 = 0
FONDO_2 = FONDO_ANCHO
VELOCIDAD_FONDO = 2

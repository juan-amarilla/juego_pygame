import pygame
from funciones import *
from constantes import *

iniciar()

pantalla = pygame.display.set_mode((800, 600))
colocar_titulo("el juego")

fuente = pygame.font.Font(None, 50)

opcion = 0

ejecutar = True

while ejecutar:

    ejecutar = menu(fuente, ejecutar)
                    
    pantalla.fill(COLOR_FONDO)

    colocar_opciones(fuente, pantalla)

    pygame.display.flip()
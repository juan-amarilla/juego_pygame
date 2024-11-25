import pygame
from funciones_menu import iniciar_con_musica, colocar_titulo
from ciclo_principal import menu

iniciar_con_musica("musica/musica_menu/ambient 9.mp3")

fuente = pygame.font.Font("fuentes/pixel.ttf", 50)

titulo = colocar_titulo("Aventura en el Lugar de Escape")

opcion = 0

ejecutar = True

while ejecutar:

    ejecutar = menu(ejecutar, fuente, titulo)
import pygame
from ciclo_principal import menu

pygame.mixer.init()
pygame.mixer.music.load("recursos_menu/musica/musica_menu/ambient 9.mp3")

ejecutar = True

while ejecutar:

    ejecutar = menu(ejecutar)